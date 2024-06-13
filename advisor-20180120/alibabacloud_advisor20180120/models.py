# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class RdAccountDTOTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class RdAccountDTO(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        checked: bool = None,
        display_name: str = None,
        id: int = None,
        name: str = None,
        tags: List[RdAccountDTOTags] = None,
    ):
        self.account_type = account_type
        self.checked = checked
        self.display_name = display_name
        self.id = id
        self.name = name
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
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.checked is not None:
            result['Checked'] = self.checked
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Checked') is not None:
            self.checked = m.get('Checked')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = RdAccountDTOTags()
                self.tags.append(temp_model.from_map(k))
        return self


class RdAccountFolderDTO(TeaModel):
    def __init__(
        self,
        account_count: int = None,
        account_list: List[RdAccountDTO] = None,
        folder_id: str = None,
        folder_list: List['RdAccountFolderDTO'] = None,
        folder_name: str = None,
        resource_directory_id: str = None,
        resource_directory_path: str = None,
        resource_directory_path_name: str = None,
        selected_count: int = None,
    ):
        self.account_count = account_count
        self.account_list = account_list
        self.folder_id = folder_id
        self.folder_list = folder_list
        self.folder_name = folder_name
        self.resource_directory_id = resource_directory_id
        self.resource_directory_path = resource_directory_path
        self.resource_directory_path_name = resource_directory_path_name
        self.selected_count = selected_count

    def validate(self):
        if self.account_list:
            for k in self.account_list:
                if k:
                    k.validate()
        if self.folder_list:
            for k in self.folder_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_count is not None:
            result['AccountCount'] = self.account_count
        result['AccountList'] = []
        if self.account_list is not None:
            for k in self.account_list:
                result['AccountList'].append(k.to_map() if k else None)
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        result['FolderList'] = []
        if self.folder_list is not None:
            for k in self.folder_list:
                result['FolderList'].append(k.to_map() if k else None)
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path
        if self.resource_directory_path_name is not None:
            result['ResourceDirectoryPathName'] = self.resource_directory_path_name
        if self.selected_count is not None:
            result['SelectedCount'] = self.selected_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountCount') is not None:
            self.account_count = m.get('AccountCount')
        self.account_list = []
        if m.get('AccountList') is not None:
            for k in m.get('AccountList'):
                temp_model = RdAccountDTO()
                self.account_list.append(temp_model.from_map(k))
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        self.folder_list = []
        if m.get('FolderList') is not None:
            for k in m.get('FolderList'):
                temp_model = RdAccountFolderDTO()
                self.folder_list.append(temp_model.from_map(k))
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')
        if m.get('ResourceDirectoryPathName') is not None:
            self.resource_directory_path_name = m.get('ResourceDirectoryPathName')
        if m.get('SelectedCount') is not None:
            self.selected_count = m.get('SelectedCount')
        return self


class DescribeAdvicesRequest(TeaModel):
    def __init__(
        self,
        advice_id: int = None,
        check_id: str = None,
        exclude_advice_id: int = None,
        language: str = None,
        product: str = None,
        resource_id: str = None,
    ):
        self.advice_id = advice_id
        self.check_id = check_id
        self.exclude_advice_id = exclude_advice_id
        self.language = language
        self.product = product
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.exclude_advice_id is not None:
            result['ExcludeAdviceId'] = self.exclude_advice_id
        if self.language is not None:
            result['Language'] = self.language
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('ExcludeAdviceId') is not None:
            self.exclude_advice_id = m.get('ExcludeAdviceId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DescribeAdvicesResponseBodyDataAdvice(TeaModel):
    def __init__(
        self,
        aliyun_id: int = None,
        check_id: str = None,
        check_name: str = None,
        content: str = None,
        description: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_expired: bool = None,
        product: str = None,
        resource: str = None,
        resource_id: str = None,
        severity: int = None,
    ):
        self.aliyun_id = aliyun_id
        self.check_id = check_id
        self.check_name = check_name
        self.content = content
        self.description = description
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        # ID
        self.id = id
        self.is_expired = is_expired
        self.product = product
        self.resource = resource
        self.resource_id = resource_id
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.product is not None:
            result['Product'] = self.product
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class DescribeAdvicesResponseBodyData(TeaModel):
    def __init__(
        self,
        advice: List[DescribeAdvicesResponseBodyDataAdvice] = None,
    ):
        self.advice = advice

    def validate(self):
        if self.advice:
            for k in self.advice:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Advice'] = []
        if self.advice is not None:
            for k in self.advice:
                result['Advice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advice = []
        if m.get('Advice') is not None:
            for k in m.get('Advice'):
                temp_model = DescribeAdvicesResponseBodyDataAdvice()
                self.advice.append(temp_model.from_map(k))
        return self


class DescribeAdvicesResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeAdvicesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeAdvicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdvicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdvicesResponseBody = None,
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
            temp_model = DescribeAdvicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdvicesFlatPageRequest(TeaModel):
    def __init__(
        self,
        advice_id: int = None,
        check_id: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        product: str = None,
        resource_id: str = None,
    ):
        self.advice_id = advice_id
        self.check_id = check_id
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.product = product
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DescribeAdvicesFlatPageResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        aliyun_id: int = None,
        check_id: str = None,
        check_name: str = None,
        content: str = None,
        description: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_expired: bool = None,
        product: str = None,
        resource: str = None,
        resource_id: str = None,
        severity: int = None,
    ):
        self.aliyun_id = aliyun_id
        self.check_id = check_id
        self.check_name = check_name
        self.content = content
        self.description = description
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_expired = is_expired
        self.product = product
        self.resource = resource
        self.resource_id = resource_id
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.product is not None:
            result['Product'] = self.product
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class DescribeAdvicesFlatPageResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        result: List[DescribeAdvicesFlatPageResponseBodyDataResult] = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.result = result
        self.total = total

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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeAdvicesFlatPageResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAdvicesFlatPageResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeAdvicesFlatPageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeAdvicesFlatPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdvicesFlatPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdvicesFlatPageResponseBody = None,
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
            temp_model = DescribeAdvicesFlatPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdvicesPageRequest(TeaModel):
    def __init__(
        self,
        advice_id: int = None,
        check_id: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        product: str = None,
        resource_id: str = None,
    ):
        self.advice_id = advice_id
        self.check_id = check_id
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.product = product
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DescribeAdvicesPageResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        aliyun_id: int = None,
        check_id: str = None,
        check_name: str = None,
        content: str = None,
        description: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_expired: bool = None,
        product: str = None,
        resource: str = None,
        resource_id: str = None,
        severity: int = None,
    ):
        self.aliyun_id = aliyun_id
        self.check_id = check_id
        self.check_name = check_name
        self.content = content
        self.description = description
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        # ID
        self.id = id
        self.is_expired = is_expired
        self.product = product
        self.resource = resource
        self.resource_id = resource_id
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.product is not None:
            result['Product'] = self.product
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class DescribeAdvicesPageResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        result: List[DescribeAdvicesPageResponseBodyDataResult] = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.result = result
        self.total = total

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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeAdvicesPageResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAdvicesPageResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeAdvicesPageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeAdvicesPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdvicesPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdvicesPageResponseBody = None,
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
            temp_model = DescribeAdvicesPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdvisorChecksRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        product: str = None,
    ):
        self.language = language
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class DescribeAdvisorChecksResponseBodyDataAdvisorCheck(TeaModel):
    def __init__(
        self,
        category: str = None,
        code: str = None,
        description: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        name: str = None,
        operate_column: str = None,
        product: str = None,
        status: str = None,
        tips: str = None,
        view_column: str = None,
    ):
        self.category = category
        self.code = code
        self.description = description
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.name = name
        self.operate_column = operate_column
        self.product = product
        self.status = status
        self.tips = tips
        self.view_column = view_column

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.operate_column is not None:
            result['OperateColumn'] = self.operate_column
        if self.product is not None:
            result['Product'] = self.product
        if self.status is not None:
            result['Status'] = self.status
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.view_column is not None:
            result['ViewColumn'] = self.view_column
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperateColumn') is not None:
            self.operate_column = m.get('OperateColumn')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('ViewColumn') is not None:
            self.view_column = m.get('ViewColumn')
        return self


class DescribeAdvisorChecksResponseBodyData(TeaModel):
    def __init__(
        self,
        advisor_check: List[DescribeAdvisorChecksResponseBodyDataAdvisorCheck] = None,
    ):
        self.advisor_check = advisor_check

    def validate(self):
        if self.advisor_check:
            for k in self.advisor_check:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdvisorCheck'] = []
        if self.advisor_check is not None:
            for k in self.advisor_check:
                result['AdvisorCheck'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advisor_check = []
        if m.get('AdvisorCheck') is not None:
            for k in m.get('AdvisorCheck'):
                temp_model = DescribeAdvisorChecksResponseBodyDataAdvisorCheck()
                self.advisor_check.append(temp_model.from_map(k))
        return self


class DescribeAdvisorChecksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeAdvisorChecksResponseBodyData = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeAdvisorChecksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdvisorChecksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdvisorChecksResponseBody = None,
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
            temp_model = DescribeAdvisorChecksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdvisorResourcesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        product: str = None,
        resource_id: str = None,
    ):
        self.keyword = keyword
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.product = product
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DescribeAdvisorResourcesResponseBodyDataResultResource(TeaModel):
    def __init__(
        self,
        data: str = None,
        product: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        self.data = data
        self.product = product
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class DescribeAdvisorResourcesResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        resource: List[DescribeAdvisorResourcesResponseBodyDataResultResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = DescribeAdvisorResourcesResponseBodyDataResultResource()
                self.resource.append(temp_model.from_map(k))
        return self


class DescribeAdvisorResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        result: DescribeAdvisorResourcesResponseBodyDataResult = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.result = result
        self.total = total

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Result') is not None:
            temp_model = DescribeAdvisorResourcesResponseBodyDataResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAdvisorResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeAdvisorResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeAdvisorResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdvisorResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdvisorResourcesResponseBody = None,
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
            temp_model = DescribeAdvisorResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCostCheckAdvicesRequest(TeaModel):
    def __init__(
        self,
        assume_aliyun_id_list: List[int] = None,
        check_id: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        region_ids: List[str] = None,
        resource_ids: List[str] = None,
        resource_name: str = None,
        severity: str = None,
        tag_keys: List[str] = None,
        tag_values: List[str] = None,
    ):
        self.assume_aliyun_id_list = assume_aliyun_id_list
        self.check_id = check_id
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.region_ids = region_ids
        self.resource_ids = resource_ids
        self.resource_name = resource_name
        self.severity = severity
        self.tag_keys = tag_keys
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_aliyun_id_list is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list = m.get('AssumeAliyunIdList')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class DescribeCostCheckAdvicesShrinkRequest(TeaModel):
    def __init__(
        self,
        assume_aliyun_id_list_shrink: str = None,
        check_id: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        region_ids_shrink: str = None,
        resource_ids_shrink: str = None,
        resource_name: str = None,
        severity: str = None,
        tag_keys_shrink: str = None,
        tag_values_shrink: str = None,
    ):
        self.assume_aliyun_id_list_shrink = assume_aliyun_id_list_shrink
        self.check_id = check_id
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.region_ids_shrink = region_ids_shrink
        self.resource_ids_shrink = resource_ids_shrink
        self.resource_name = resource_name
        self.severity = severity
        self.tag_keys_shrink = tag_keys_shrink
        self.tag_values_shrink = tag_values_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_aliyun_id_list_shrink is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list_shrink
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink
        if self.tag_values_shrink is not None:
            result['TagValues'] = self.tag_values_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list_shrink = m.get('AssumeAliyunIdList')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')
        if m.get('TagValues') is not None:
            self.tag_values_shrink = m.get('TagValues')
        return self


class DescribeCostCheckAdvicesResponseBodyDataAdviceListTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeCostCheckAdvicesResponseBodyDataAdviceList(TeaModel):
    def __init__(
        self,
        account_folder_id: str = None,
        account_folder_name: str = None,
        aliyun_id: int = None,
        content: str = None,
        email: str = None,
        end_time: int = None,
        gmt_deleted: int = None,
        product: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        severity: str = None,
        start_time: int = None,
        tags: List[DescribeCostCheckAdvicesResponseBodyDataAdviceListTags] = None,
        url: str = None,
        user_name: str = None,
        zone_id: str = None,
    ):
        self.account_folder_id = account_folder_id
        self.account_folder_name = account_folder_name
        self.aliyun_id = aliyun_id
        self.content = content
        self.email = email
        self.end_time = end_time
        self.gmt_deleted = gmt_deleted
        self.product = product
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.severity = severity
        self.start_time = start_time
        self.tags = tags
        self.url = url
        self.user_name = user_name
        self.zone_id = zone_id

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
        if self.account_folder_id is not None:
            result['AccountFolderId'] = self.account_folder_id
        if self.account_folder_name is not None:
            result['AccountFolderName'] = self.account_folder_name
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.content is not None:
            result['Content'] = self.content
        if self.email is not None:
            result['Email'] = self.email
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_deleted is not None:
            result['GmtDeleted'] = self.gmt_deleted
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.url is not None:
            result['Url'] = self.url
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountFolderId') is not None:
            self.account_folder_id = m.get('AccountFolderId')
        if m.get('AccountFolderName') is not None:
            self.account_folder_name = m.get('AccountFolderName')
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtDeleted') is not None:
            self.gmt_deleted = m.get('GmtDeleted')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeCostCheckAdvicesResponseBodyDataAdviceListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeCostCheckAdvicesResponseBodyData(TeaModel):
    def __init__(
        self,
        advice_list: List[DescribeCostCheckAdvicesResponseBodyDataAdviceList] = None,
        check_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.advice_list = advice_list
        self.check_id = check_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.advice_list:
            for k in self.advice_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdviceList'] = []
        if self.advice_list is not None:
            for k in self.advice_list:
                result['AdviceList'].append(k.to_map() if k else None)
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advice_list = []
        if m.get('AdviceList') is not None:
            for k in m.get('AdviceList'):
                temp_model = DescribeCostCheckAdvicesResponseBodyDataAdviceList()
                self.advice_list.append(temp_model.from_map(k))
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCostCheckAdvicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCostCheckAdvicesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeCostCheckAdvicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCostCheckAdvicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCostCheckAdvicesResponseBody = None,
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
            temp_model = DescribeCostCheckAdvicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCostCheckResultsRequest(TeaModel):
    def __init__(
        self,
        assume_aliyun_id_list: List[int] = None,
        check_ids: List[str] = None,
        group_by: str = None,
        product: str = None,
        region_ids: List[str] = None,
        resource_ids: List[str] = None,
        resource_name: str = None,
        severity: int = None,
        tag_keys: List[str] = None,
        tag_values: List[str] = None,
    ):
        self.assume_aliyun_id_list = assume_aliyun_id_list
        self.check_ids = check_ids
        self.group_by = group_by
        self.product = product
        self.region_ids = region_ids
        self.resource_ids = resource_ids
        self.resource_name = resource_name
        self.severity = severity
        self.tag_keys = tag_keys
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_aliyun_id_list is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.product is not None:
            result['Product'] = self.product
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list = m.get('AssumeAliyunIdList')
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class DescribeCostCheckResultsShrinkRequest(TeaModel):
    def __init__(
        self,
        assume_aliyun_id_list_shrink: str = None,
        check_ids_shrink: str = None,
        group_by: str = None,
        product: str = None,
        region_ids_shrink: str = None,
        resource_ids_shrink: str = None,
        resource_name: str = None,
        severity: int = None,
        tag_keys_shrink: str = None,
        tag_values_shrink: str = None,
    ):
        self.assume_aliyun_id_list_shrink = assume_aliyun_id_list_shrink
        self.check_ids_shrink = check_ids_shrink
        self.group_by = group_by
        self.product = product
        self.region_ids_shrink = region_ids_shrink
        self.resource_ids_shrink = resource_ids_shrink
        self.resource_name = resource_name
        self.severity = severity
        self.tag_keys_shrink = tag_keys_shrink
        self.tag_values_shrink = tag_values_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_aliyun_id_list_shrink is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list_shrink
        if self.check_ids_shrink is not None:
            result['CheckIds'] = self.check_ids_shrink
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.product is not None:
            result['Product'] = self.product
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink
        if self.tag_values_shrink is not None:
            result['TagValues'] = self.tag_values_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list_shrink = m.get('AssumeAliyunIdList')
        if m.get('CheckIds') is not None:
            self.check_ids_shrink = m.get('CheckIds')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')
        if m.get('TagValues') is not None:
            self.tag_values_shrink = m.get('TagValues')
        return self


class DescribeCostCheckResultsResponseBodyDataViewGroupCheckItems(TeaModel):
    def __init__(
        self,
        advice_count: int = None,
        advice_resource_count: int = None,
        category: str = None,
        check_id: str = None,
        check_name: str = None,
        current_cost: float = None,
        description: str = None,
        expected_saving_cost: float = None,
        optimized_cost: float = None,
        product: str = None,
        severity: int = None,
        summary: str = None,
        tips: str = None,
    ):
        self.advice_count = advice_count
        self.advice_resource_count = advice_resource_count
        self.category = category
        self.check_id = check_id
        self.check_name = check_name
        self.current_cost = current_cost
        self.description = description
        self.expected_saving_cost = expected_saving_cost
        self.optimized_cost = optimized_cost
        self.product = product
        self.severity = severity
        self.summary = summary
        self.tips = tips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_count is not None:
            result['AdviceCount'] = self.advice_count
        if self.advice_resource_count is not None:
            result['AdviceResourceCount'] = self.advice_resource_count
        if self.category is not None:
            result['Category'] = self.category
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.current_cost is not None:
            result['CurrentCost'] = self.current_cost
        if self.description is not None:
            result['Description'] = self.description
        if self.expected_saving_cost is not None:
            result['ExpectedSavingCost'] = self.expected_saving_cost
        if self.optimized_cost is not None:
            result['OptimizedCost'] = self.optimized_cost
        if self.product is not None:
            result['Product'] = self.product
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceCount') is not None:
            self.advice_count = m.get('AdviceCount')
        if m.get('AdviceResourceCount') is not None:
            self.advice_resource_count = m.get('AdviceResourceCount')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CurrentCost') is not None:
            self.current_cost = m.get('CurrentCost')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpectedSavingCost') is not None:
            self.expected_saving_cost = m.get('ExpectedSavingCost')
        if m.get('OptimizedCost') is not None:
            self.optimized_cost = m.get('OptimizedCost')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class DescribeCostCheckResultsResponseBodyDataViewGroup(TeaModel):
    def __init__(
        self,
        check_items: List[DescribeCostCheckResultsResponseBodyDataViewGroupCheckItems] = None,
        group_code: str = None,
        group_count: int = None,
        group_expected_saving_cost: float = None,
        group_name: str = None,
    ):
        self.check_items = check_items
        self.group_code = group_code
        self.group_count = group_count
        self.group_expected_saving_cost = group_expected_saving_cost
        self.group_name = group_name

    def validate(self):
        if self.check_items:
            for k in self.check_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckItems'] = []
        if self.check_items is not None:
            for k in self.check_items:
                result['CheckItems'].append(k.to_map() if k else None)
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_count is not None:
            result['GroupCount'] = self.group_count
        if self.group_expected_saving_cost is not None:
            result['GroupExpectedSavingCost'] = self.group_expected_saving_cost
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_items = []
        if m.get('CheckItems') is not None:
            for k in m.get('CheckItems'):
                temp_model = DescribeCostCheckResultsResponseBodyDataViewGroupCheckItems()
                self.check_items.append(temp_model.from_map(k))
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')
        if m.get('GroupExpectedSavingCost') is not None:
            self.group_expected_saving_cost = m.get('GroupExpectedSavingCost')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeCostCheckResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        advice_resource_count: int = None,
        group_by: str = None,
        normal_count: int = None,
        resource_count: int = None,
        total_count: int = None,
        view_group: List[DescribeCostCheckResultsResponseBodyDataViewGroup] = None,
        warning_count: int = None,
    ):
        self.advice_resource_count = advice_resource_count
        self.group_by = group_by
        self.normal_count = normal_count
        self.resource_count = resource_count
        self.total_count = total_count
        self.view_group = view_group
        self.warning_count = warning_count

    def validate(self):
        if self.view_group:
            for k in self.view_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_resource_count is not None:
            result['AdviceResourceCount'] = self.advice_resource_count
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.normal_count is not None:
            result['NormalCount'] = self.normal_count
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ViewGroup'] = []
        if self.view_group is not None:
            for k in self.view_group:
                result['ViewGroup'].append(k.to_map() if k else None)
        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceResourceCount') is not None:
            self.advice_resource_count = m.get('AdviceResourceCount')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('NormalCount') is not None:
            self.normal_count = m.get('NormalCount')
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.view_group = []
        if m.get('ViewGroup') is not None:
            for k in m.get('ViewGroup'):
                temp_model = DescribeCostCheckResultsResponseBodyDataViewGroup()
                self.view_group.append(temp_model.from_map(k))
        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')
        return self


class DescribeCostCheckResultsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCostCheckResultsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeCostCheckResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCostCheckResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCostCheckResultsResponseBody = None,
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
            temp_model = DescribeCostCheckResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistoryAdvicesRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        language: str = None,
        page_num: int = None,
        page_size: int = None,
        product: str = None,
        reverse: bool = None,
        severity: str = None,
        start_date: str = None,
    ):
        self.end_date = end_date
        self.language = language
        self.page_num = page_num
        self.page_size = page_size
        self.product = product
        self.reverse = reverse
        self.severity = severity
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.language is not None:
            result['Language'] = self.language
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetHistoryAdvicesResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        check_id: str = None,
        check_name: str = None,
        description: str = None,
        gmt_created: str = None,
        product: str = None,
        resource_id: str = None,
        severity: int = None,
        url: str = None,
    ):
        self.check_id = check_id
        self.check_name = check_name
        self.description = description
        self.gmt_created = gmt_created
        self.product = product
        self.resource_id = resource_id
        self.severity = severity
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetHistoryAdvicesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        result: List[GetHistoryAdvicesResponseBodyDataResult] = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.result = result
        self.total = total

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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetHistoryAdvicesResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetHistoryAdvicesResponseBody(TeaModel):
    def __init__(
        self,
        data: GetHistoryAdvicesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetHistoryAdvicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHistoryAdvicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHistoryAdvicesResponseBody = None,
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
            temp_model = GetHistoryAdvicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusByIdRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskStatusByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        task_status: int = None,
    ):
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetTaskStatusByIdResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTaskStatusByIdResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTaskStatusByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTaskStatusByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskStatusByIdResponseBody = None,
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
            temp_model = GetTaskStatusByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshAdvisorCheckRequest(TeaModel):
    def __init__(
        self,
        check_id: str = None,
        language: str = None,
        product: str = None,
        resource_id: str = None,
    ):
        self.check_id = check_id
        self.language = language
        self.product = product
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.language is not None:
            result['Language'] = self.language
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class RefreshAdvisorCheckResponseBodyData(TeaModel):
    def __init__(
        self,
        success: bool = None,
        task_id: int = None,
        trace_id: str = None,
    ):
        self.success = success
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RefreshAdvisorCheckResponseBody(TeaModel):
    def __init__(
        self,
        data: RefreshAdvisorCheckResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RefreshAdvisorCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshAdvisorCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshAdvisorCheckResponseBody = None,
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
            temp_model = RefreshAdvisorCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshAdvisorCostCheckRequest(TeaModel):
    def __init__(
        self,
        assume_aliyun_id_list: List[int] = None,
        check_ids: List[str] = None,
        product: str = None,
        refresh_resource: bool = None,
        resource_ids: List[str] = None,
    ):
        self.assume_aliyun_id_list = assume_aliyun_id_list
        self.check_ids = check_ids
        self.product = product
        self.refresh_resource = refresh_resource
        self.resource_ids = resource_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_aliyun_id_list is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids
        if self.product is not None:
            result['Product'] = self.product
        if self.refresh_resource is not None:
            result['RefreshResource'] = self.refresh_resource
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list = m.get('AssumeAliyunIdList')
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RefreshResource') is not None:
            self.refresh_resource = m.get('RefreshResource')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        return self


class RefreshAdvisorCostCheckShrinkRequest(TeaModel):
    def __init__(
        self,
        assume_aliyun_id_list_shrink: str = None,
        check_ids_shrink: str = None,
        product: str = None,
        refresh_resource: bool = None,
        resource_ids_shrink: str = None,
    ):
        self.assume_aliyun_id_list_shrink = assume_aliyun_id_list_shrink
        self.check_ids_shrink = check_ids_shrink
        self.product = product
        self.refresh_resource = refresh_resource
        self.resource_ids_shrink = resource_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_aliyun_id_list_shrink is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list_shrink
        if self.check_ids_shrink is not None:
            result['CheckIds'] = self.check_ids_shrink
        if self.product is not None:
            result['Product'] = self.product
        if self.refresh_resource is not None:
            result['RefreshResource'] = self.refresh_resource
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list_shrink = m.get('AssumeAliyunIdList')
        if m.get('CheckIds') is not None:
            self.check_ids_shrink = m.get('CheckIds')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RefreshResource') is not None:
            self.refresh_resource = m.get('RefreshResource')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        return self


class RefreshAdvisorCostCheckResponseBodyData(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        manager_task_id: int = None,
        success: bool = None,
        task_id: int = None,
    ):
        self.command_id = command_id
        self.manager_task_id = manager_task_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.manager_task_id is not None:
            result['ManagerTaskId'] = self.manager_task_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('ManagerTaskId') is not None:
            self.manager_task_id = m.get('ManagerTaskId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RefreshAdvisorCostCheckResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RefreshAdvisorCostCheckResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = RefreshAdvisorCostCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshAdvisorCostCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshAdvisorCostCheckResponseBody = None,
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
            temp_model = RefreshAdvisorCostCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshAdvisorResourceRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        resource_id: str = None,
    ):
        # This parameter is required.
        self.product = product
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class RefreshAdvisorResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshAdvisorResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshAdvisorResourceResponseBody = None,
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
            temp_model = RefreshAdvisorResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportBizAlertInfoRequest(TeaModel):
    def __init__(
        self,
        alert_description: str = None,
        alert_detail: str = None,
        alert_grade: str = None,
        alert_labels: str = None,
        alert_scene: str = None,
        alert_token: str = None,
        alert_uid: List[int] = None,
        language: str = None,
    ):
        self.alert_description = alert_description
        # This parameter is required.
        self.alert_detail = alert_detail
        self.alert_grade = alert_grade
        self.alert_labels = alert_labels
        # This parameter is required.
        self.alert_scene = alert_scene
        # This parameter is required.
        self.alert_token = alert_token
        self.alert_uid = alert_uid
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_description is not None:
            result['AlertDescription'] = self.alert_description
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        if self.alert_grade is not None:
            result['AlertGrade'] = self.alert_grade
        if self.alert_labels is not None:
            result['AlertLabels'] = self.alert_labels
        if self.alert_scene is not None:
            result['AlertScene'] = self.alert_scene
        if self.alert_token is not None:
            result['AlertToken'] = self.alert_token
        if self.alert_uid is not None:
            result['AlertUid'] = self.alert_uid
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDescription') is not None:
            self.alert_description = m.get('AlertDescription')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        if m.get('AlertGrade') is not None:
            self.alert_grade = m.get('AlertGrade')
        if m.get('AlertLabels') is not None:
            self.alert_labels = m.get('AlertLabels')
        if m.get('AlertScene') is not None:
            self.alert_scene = m.get('AlertScene')
        if m.get('AlertToken') is not None:
            self.alert_token = m.get('AlertToken')
        if m.get('AlertUid') is not None:
            self.alert_uid = m.get('AlertUid')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ReportBizAlertInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        alert_description: str = None,
        alert_detail: str = None,
        alert_grade: str = None,
        alert_labels: str = None,
        alert_scene: str = None,
        alert_token: str = None,
        alert_uid_shrink: str = None,
        language: str = None,
    ):
        self.alert_description = alert_description
        # This parameter is required.
        self.alert_detail = alert_detail
        self.alert_grade = alert_grade
        self.alert_labels = alert_labels
        # This parameter is required.
        self.alert_scene = alert_scene
        # This parameter is required.
        self.alert_token = alert_token
        self.alert_uid_shrink = alert_uid_shrink
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_description is not None:
            result['AlertDescription'] = self.alert_description
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        if self.alert_grade is not None:
            result['AlertGrade'] = self.alert_grade
        if self.alert_labels is not None:
            result['AlertLabels'] = self.alert_labels
        if self.alert_scene is not None:
            result['AlertScene'] = self.alert_scene
        if self.alert_token is not None:
            result['AlertToken'] = self.alert_token
        if self.alert_uid_shrink is not None:
            result['AlertUid'] = self.alert_uid_shrink
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDescription') is not None:
            self.alert_description = m.get('AlertDescription')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        if m.get('AlertGrade') is not None:
            self.alert_grade = m.get('AlertGrade')
        if m.get('AlertLabels') is not None:
            self.alert_labels = m.get('AlertLabels')
        if m.get('AlertScene') is not None:
            self.alert_scene = m.get('AlertScene')
        if m.get('AlertToken') is not None:
            self.alert_token = m.get('AlertToken')
        if m.get('AlertUid') is not None:
            self.alert_uid_shrink = m.get('AlertUid')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ReportBizAlertInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ReportBizAlertInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ReportBizAlertInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = ReportBizAlertInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReportBizAlertInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportBizAlertInfoResponseBody = None,
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
            temp_model = ReportBizAlertInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


