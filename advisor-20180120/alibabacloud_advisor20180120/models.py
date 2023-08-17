# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DescribeAdvicesRequest(TeaModel):
    def __init__(
        self,
        advice_id: int = None,
        check_id: str = None,
        client_uid: int = None,
        exclude_advice_id: int = None,
        filter_type: str = None,
        filter_value: str = None,
        language: str = None,
        product: str = None,
        region: str = None,
        resource_id: str = None,
        token: str = None,
    ):
        self.advice_id = advice_id
        self.check_id = check_id
        self.client_uid = client_uid
        self.exclude_advice_id = exclude_advice_id
        self.filter_type = filter_type
        self.filter_value = filter_value
        self.language = language
        self.product = product
        self.region = region
        self.resource_id = resource_id
        self.token = token

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
        if self.client_uid is not None:
            result['ClientUid'] = self.client_uid
        if self.exclude_advice_id is not None:
            result['ExcludeAdviceId'] = self.exclude_advice_id
        if self.filter_type is not None:
            result['FilterType'] = self.filter_type
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.language is not None:
            result['Language'] = self.language
        if self.product is not None:
            result['Product'] = self.product
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('ClientUid') is not None:
            self.client_uid = m.get('ClientUid')
        if m.get('ExcludeAdviceId') is not None:
            self.exclude_advice_id = m.get('ExcludeAdviceId')
        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeAdvicesResponseBodyDataAdvice(TeaModel):
    def __init__(
        self,
        action: str = None,
        aliyun_id: int = None,
        check_id: str = None,
        check_name: str = None,
        content: str = None,
        description: str = None,
        details: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_expired: bool = None,
        links: str = None,
        product: str = None,
        reason: str = None,
        resource: str = None,
        resource_id: str = None,
        severity: int = None,
    ):
        self.action = action
        self.aliyun_id = aliyun_id
        self.check_id = check_id
        self.check_name = check_name
        self.content = content
        self.description = description
        self.details = details
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        # ID
        self.id = id
        self.is_expired = is_expired
        self.links = links
        self.product = product
        self.reason = reason
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
        if self.action is not None:
            result['Action'] = self.action
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
        if self.details is not None:
            result['Details'] = self.details
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.links is not None:
            result['Links'] = self.links
        if self.product is not None:
            result['Product'] = self.product
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class DescribeAdvicesPageRequest(TeaModel):
    def __init__(
        self,
        advice_id: int = None,
        associate_uid: int = None,
        check_id: str = None,
        exclude_advice_id: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        product: str = None,
        resource_id: str = None,
    ):
        self.advice_id = advice_id
        self.associate_uid = associate_uid
        self.check_id = check_id
        self.exclude_advice_id = exclude_advice_id
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
        if self.associate_uid is not None:
            result['AssociateUid'] = self.associate_uid
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.exclude_advice_id is not None:
            result['ExcludeAdviceId'] = self.exclude_advice_id
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
        if m.get('AssociateUid') is not None:
            self.associate_uid = m.get('AssociateUid')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('ExcludeAdviceId') is not None:
            self.exclude_advice_id = m.get('ExcludeAdviceId')
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
        action: str = None,
        aliyun_id: int = None,
        check_id: str = None,
        check_name: str = None,
        content: str = None,
        description: str = None,
        details: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_expired: bool = None,
        links: str = None,
        product: str = None,
        reason: str = None,
        resource: str = None,
        resource_id: str = None,
        severity: int = None,
    ):
        self.action = action
        self.aliyun_id = aliyun_id
        self.check_id = check_id
        self.check_name = check_name
        self.content = content
        self.description = description
        self.details = details
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        # ID
        self.id = id
        self.is_expired = is_expired
        self.links = links
        self.product = product
        self.reason = reason
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
        if self.action is not None:
            result['Action'] = self.action
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
        if self.details is not None:
            result['Details'] = self.details
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.links is not None:
            result['Links'] = self.links
        if self.product is not None:
            result['Product'] = self.product
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class DescribeAdvisorChecksResponseBodyDataAdvisorCheck(TeaModel):
    def __init__(
        self,
        category: str = None,
        code: str = None,
        description: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        operate_column: str = None,
        product: str = None,
        status: str = None,
        supp_resources: str = None,
        tips: str = None,
        view_column: str = None,
    ):
        self.category = category
        self.code = code
        self.description = description
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        # ID
        self.id = id
        self.name = name
        self.operate_column = operate_column
        self.product = product
        self.status = status
        self.supp_resources = supp_resources
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
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.operate_column is not None:
            result['OperateColumn'] = self.operate_column
        if self.product is not None:
            result['Product'] = self.product
        if self.status is not None:
            result['Status'] = self.status
        if self.supp_resources is not None:
            result['SuppResources'] = self.supp_resources
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
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperateColumn') is not None:
            self.operate_column = m.get('OperateColumn')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuppResources') is not None:
            self.supp_resources = m.get('SuppResources')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class GetHistoryAdvicesRequest(TeaModel):
    def __init__(
        self,
        associate_uid: int = None,
        check_id: str = None,
        client_uid: int = None,
        end_date: str = None,
        filter_type: str = None,
        filter_value: str = None,
        is_expired: bool = None,
        language: str = None,
        page_num: int = None,
        page_size: int = None,
        product: str = None,
        region: str = None,
        resource_id: str = None,
        reverse: bool = None,
        severity: str = None,
        start_date: str = None,
    ):
        self.associate_uid = associate_uid
        self.check_id = check_id
        self.client_uid = client_uid
        self.end_date = end_date
        self.filter_type = filter_type
        self.filter_value = filter_value
        self.is_expired = is_expired
        self.language = language
        self.page_num = page_num
        self.page_size = page_size
        self.product = product
        self.region = region
        self.resource_id = resource_id
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
        if self.associate_uid is not None:
            result['AssociateUid'] = self.associate_uid
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.client_uid is not None:
            result['ClientUid'] = self.client_uid
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.filter_type is not None:
            result['FilterType'] = self.filter_type
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.language is not None:
            result['Language'] = self.language
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociateUid') is not None:
            self.associate_uid = m.get('AssociateUid')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('ClientUid') is not None:
            self.client_uid = m.get('ClientUid')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class RefreshAdvisorResourceRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        resource_id: str = None,
    ):
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


