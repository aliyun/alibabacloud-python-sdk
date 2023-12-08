# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class Address(TeaModel):
    def __init__(
        self,
        city_code: str = None,
        detail: str = None,
        district_code: str = None,
        province_code: str = None,
    ):
        self.city_code = city_code
        self.detail = detail
        self.district_code = district_code
        self.province_code = province_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_code is not None:
            result['cityCode'] = self.city_code
        if self.detail is not None:
            result['detail'] = self.detail
        if self.district_code is not None:
            result['districtCode'] = self.district_code
        if self.province_code is not None:
            result['provinceCode'] = self.province_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cityCode') is not None:
            self.city_code = m.get('cityCode')
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('districtCode') is not None:
            self.district_code = m.get('districtCode')
        if m.get('provinceCode') is not None:
            self.province_code = m.get('provinceCode')
        return self


class Company(TeaModel):
    def __init__(
        self,
        name: str = None,
        uscc: str = None,
    ):
        self.name = name
        self.uscc = uscc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.uscc is not None:
            result['uscc'] = self.uscc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uscc') is not None:
            self.uscc = m.get('uscc')
        return self


class Contact(TeaModel):
    def __init__(
        self,
        email: str = None,
        name: str = None,
        phone: str = None,
    ):
        self.email = email
        self.name = name
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.name is not None:
            result['name'] = self.name
        if self.phone is not None:
            result['phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        return self


class ExtendInfo(TeaModel):
    def __init__(
        self,
        deposit_amount: float = None,
        desc: str = None,
    ):
        self.deposit_amount = deposit_amount
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deposit_amount is not None:
            result['depositAmount'] = self.deposit_amount
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('depositAmount') is not None:
            self.deposit_amount = m.get('depositAmount')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self


class SubjectExtendInfo(TeaModel):
    def __init__(
        self,
        delivery_desc: str = None,
        desc: str = None,
    ):
        self.delivery_desc = delivery_desc
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_desc is not None:
            result['deliveryDesc'] = self.delivery_desc
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deliveryDesc') is not None:
            self.delivery_desc = m.get('deliveryDesc')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self


class CreateSourcingProjectRequestAddress(TeaModel):
    def __init__(
        self,
        city_code: str = None,
        detail: str = None,
        district_code: str = None,
        province_code: str = None,
    ):
        self.city_code = city_code
        self.detail = detail
        self.district_code = district_code
        self.province_code = province_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.district_code is not None:
            result['DistrictCode'] = self.district_code
        if self.province_code is not None:
            result['ProvinceCode'] = self.province_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DistrictCode') is not None:
            self.district_code = m.get('DistrictCode')
        if m.get('ProvinceCode') is not None:
            self.province_code = m.get('ProvinceCode')
        return self


class CreateSourcingProjectRequestCompany(TeaModel):
    def __init__(
        self,
        name: str = None,
        uscc: str = None,
    ):
        self.name = name
        self.uscc = uscc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.uscc is not None:
            result['Uscc'] = self.uscc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uscc') is not None:
            self.uscc = m.get('Uscc')
        return self


class CreateSourcingProjectRequestContact(TeaModel):
    def __init__(
        self,
        email: str = None,
        name: str = None,
        phone: str = None,
    ):
        self.email = email
        self.name = name
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.name is not None:
            result['Name'] = self.name
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class CreateSourcingProjectRequestSubjectsAddress(TeaModel):
    def __init__(
        self,
        city_code: str = None,
        detail: str = None,
        district_code: str = None,
        province_code: str = None,
    ):
        self.city_code = city_code
        self.detail = detail
        self.district_code = district_code
        self.province_code = province_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.district_code is not None:
            result['DistrictCode'] = self.district_code
        if self.province_code is not None:
            result['ProvinceCode'] = self.province_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DistrictCode') is not None:
            self.district_code = m.get('DistrictCode')
        if m.get('ProvinceCode') is not None:
            self.province_code = m.get('ProvinceCode')
        return self


class CreateSourcingProjectRequestSubjects(TeaModel):
    def __init__(
        self,
        address: CreateSourcingProjectRequestSubjectsAddress = None,
        code: str = None,
        extend_info: Dict[str, str] = None,
        name: str = None,
        quantity: float = None,
        spec: str = None,
        unit: str = None,
    ):
        self.address = address
        self.code = code
        self.extend_info = extend_info
        self.name = name
        self.quantity = quantity
        self.spec = spec
        self.unit = unit

    def validate(self):
        if self.address:
            self.address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.name is not None:
            result['Name'] = self.name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = CreateSourcingProjectRequestSubjectsAddress()
            self.address = temp_model.from_map(m['Address'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class CreateSourcingProjectRequest(TeaModel):
    def __init__(
        self,
        address: CreateSourcingProjectRequestAddress = None,
        biz_id: str = None,
        biz_no: str = None,
        biz_type: str = None,
        company: CreateSourcingProjectRequestCompany = None,
        contact: CreateSourcingProjectRequestContact = None,
        create_time: str = None,
        expire_time: str = None,
        extend_info: Dict[str, str] = None,
        source_url: str = None,
        sub_biz_type: str = None,
        subjects: List[CreateSourcingProjectRequestSubjects] = None,
        title: str = None,
    ):
        self.address = address
        self.biz_id = biz_id
        self.biz_no = biz_no
        self.biz_type = biz_type
        self.company = company
        self.contact = contact
        self.create_time = create_time
        self.expire_time = expire_time
        self.extend_info = extend_info
        self.source_url = source_url
        self.sub_biz_type = sub_biz_type
        self.subjects = subjects
        self.title = title

    def validate(self):
        if self.address:
            self.address.validate()
        if self.company:
            self.company.validate()
        if self.contact:
            self.contact.validate()
        if self.subjects:
            for k in self.subjects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_no is not None:
            result['BizNo'] = self.biz_no
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.company is not None:
            result['Company'] = self.company.to_map()
        if self.contact is not None:
            result['Contact'] = self.contact.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.sub_biz_type is not None:
            result['SubBizType'] = self.sub_biz_type
        result['Subjects'] = []
        if self.subjects is not None:
            for k in self.subjects:
                result['Subjects'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = CreateSourcingProjectRequestAddress()
            self.address = temp_model.from_map(m['Address'])
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizNo') is not None:
            self.biz_no = m.get('BizNo')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Company') is not None:
            temp_model = CreateSourcingProjectRequestCompany()
            self.company = temp_model.from_map(m['Company'])
        if m.get('Contact') is not None:
            temp_model = CreateSourcingProjectRequestContact()
            self.contact = temp_model.from_map(m['Contact'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('SubBizType') is not None:
            self.sub_biz_type = m.get('SubBizType')
        self.subjects = []
        if m.get('Subjects') is not None:
            for k in m.get('Subjects'):
                temp_model = CreateSourcingProjectRequestSubjects()
                self.subjects.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateSourcingProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        address_shrink: str = None,
        biz_id: str = None,
        biz_no: str = None,
        biz_type: str = None,
        company_shrink: str = None,
        contact_shrink: str = None,
        create_time: str = None,
        expire_time: str = None,
        extend_info_shrink: str = None,
        source_url: str = None,
        sub_biz_type: str = None,
        subjects_shrink: str = None,
        title: str = None,
    ):
        self.address_shrink = address_shrink
        self.biz_id = biz_id
        self.biz_no = biz_no
        self.biz_type = biz_type
        self.company_shrink = company_shrink
        self.contact_shrink = contact_shrink
        self.create_time = create_time
        self.expire_time = expire_time
        self.extend_info_shrink = extend_info_shrink
        self.source_url = source_url
        self.sub_biz_type = sub_biz_type
        self.subjects_shrink = subjects_shrink
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_shrink is not None:
            result['Address'] = self.address_shrink
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_no is not None:
            result['BizNo'] = self.biz_no
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.company_shrink is not None:
            result['Company'] = self.company_shrink
        if self.contact_shrink is not None:
            result['Contact'] = self.contact_shrink
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.extend_info_shrink is not None:
            result['ExtendInfo'] = self.extend_info_shrink
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.sub_biz_type is not None:
            result['SubBizType'] = self.sub_biz_type
        if self.subjects_shrink is not None:
            result['Subjects'] = self.subjects_shrink
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address_shrink = m.get('Address')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizNo') is not None:
            self.biz_no = m.get('BizNo')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Company') is not None:
            self.company_shrink = m.get('Company')
        if m.get('Contact') is not None:
            self.contact_shrink = m.get('Contact')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info_shrink = m.get('ExtendInfo')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('SubBizType') is not None:
            self.sub_biz_type = m.get('SubBizType')
        if m.get('Subjects') is not None:
            self.subjects_shrink = m.get('Subjects')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateSourcingProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSourcingProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSourcingProjectResponseBody = None,
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
            temp_model = CreateSourcingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSourcingProjectRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.biz_id = biz_id
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateSourcingProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSourcingProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSourcingProjectResponseBody = None,
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
            temp_model = UpdateSourcingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


