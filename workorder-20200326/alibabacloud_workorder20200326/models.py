# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CloseTicketRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        ticket_id: str = None,
    ):
        self.language = language
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class CloseTicketResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseTicketResponseBody = None,
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
            temp_model = CloseTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTicketRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        title: str = None,
        content: str = None,
        secret_content: str = None,
        product_code: str = None,
        category: str = None,
        phone: str = None,
        email: str = None,
        notify_time_range: str = None,
    ):
        self.language = language
        self.title = title
        self.content = content
        self.secret_content = secret_content
        self.product_code = product_code
        self.category = category
        self.phone = phone
        self.email = email
        self.notify_time_range = notify_time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.title is not None:
            result['Title'] = self.title
        if self.content is not None:
            result['Content'] = self.content
        if self.secret_content is not None:
            result['SecretContent'] = self.secret_content
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.category is not None:
            result['Category'] = self.category
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.email is not None:
            result['Email'] = self.email
        if self.notify_time_range is not None:
            result['NotifyTimeRange'] = self.notify_time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('SecretContent') is not None:
            self.secret_content = m.get('SecretContent')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('NotifyTimeRange') is not None:
            self.notify_time_range = m.get('NotifyTimeRange')
        return self


class CreateTicketResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTicketResponseBody = None,
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
            temp_model = CreateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCategoriesRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        product_code: str = None,
    ):
        self.language = language
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListCategoriesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: int = None,
    ):
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListCategoriesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListCategoriesResponseBodyDataList] = None,
    ):
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListCategoriesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class ListCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListCategoriesResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListCategoriesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCategoriesResponseBody = None,
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
            temp_model = ListCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
    ):
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ListProductsResponseBodyDataHotConsultation(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        product_code: str = None,
    ):
        self.description = description
        self.name = name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductsResponseBodyDataConsultationMore(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        product_code: str = None,
    ):
        self.description = description
        self.name = name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductsResponseBodyDataHotTech(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        product_code: str = None,
    ):
        self.description = description
        self.name = name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductsResponseBodyDataTechMoreProductList(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        product_code: str = None,
    ):
        self.description = description
        self.name = name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductsResponseBodyDataTechMore(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        product_list: List[ListProductsResponseBodyDataTechMoreProductList] = None,
    ):
        self.group_name = group_name
        self.product_list = product_list

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = ListProductsResponseBodyDataTechMoreProductList()
                self.product_list.append(temp_model.from_map(k))
        return self


class ListProductsResponseBodyData(TeaModel):
    def __init__(
        self,
        hot_consultation: List[ListProductsResponseBodyDataHotConsultation] = None,
        consultation_more: List[ListProductsResponseBodyDataConsultationMore] = None,
        hot_tech: List[ListProductsResponseBodyDataHotTech] = None,
        tech_more: List[ListProductsResponseBodyDataTechMore] = None,
    ):
        self.hot_consultation = hot_consultation
        self.consultation_more = consultation_more
        self.hot_tech = hot_tech
        self.tech_more = tech_more

    def validate(self):
        if self.hot_consultation:
            for k in self.hot_consultation:
                if k:
                    k.validate()
        if self.consultation_more:
            for k in self.consultation_more:
                if k:
                    k.validate()
        if self.hot_tech:
            for k in self.hot_tech:
                if k:
                    k.validate()
        if self.tech_more:
            for k in self.tech_more:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HotConsultation'] = []
        if self.hot_consultation is not None:
            for k in self.hot_consultation:
                result['HotConsultation'].append(k.to_map() if k else None)
        result['ConsultationMore'] = []
        if self.consultation_more is not None:
            for k in self.consultation_more:
                result['ConsultationMore'].append(k.to_map() if k else None)
        result['HotTech'] = []
        if self.hot_tech is not None:
            for k in self.hot_tech:
                result['HotTech'].append(k.to_map() if k else None)
        result['TechMore'] = []
        if self.tech_more is not None:
            for k in self.tech_more:
                result['TechMore'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hot_consultation = []
        if m.get('HotConsultation') is not None:
            for k in m.get('HotConsultation'):
                temp_model = ListProductsResponseBodyDataHotConsultation()
                self.hot_consultation.append(temp_model.from_map(k))
        self.consultation_more = []
        if m.get('ConsultationMore') is not None:
            for k in m.get('ConsultationMore'):
                temp_model = ListProductsResponseBodyDataConsultationMore()
                self.consultation_more.append(temp_model.from_map(k))
        self.hot_tech = []
        if m.get('HotTech') is not None:
            for k in m.get('HotTech'):
                temp_model = ListProductsResponseBodyDataHotTech()
                self.hot_tech.append(temp_model.from_map(k))
        self.tech_more = []
        if m.get('TechMore') is not None:
            for k in m.get('TechMore'):
                temp_model = ListProductsResponseBodyDataTechMore()
                self.tech_more.append(temp_model.from_map(k))
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListProductsResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListProductsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProductsResponseBody = None,
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
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTicketNotesRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        ticket_id: str = None,
    ):
        self.language = language
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class ListTicketNotesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        gmt_created: int = None,
        note_id: str = None,
        from_official: bool = None,
        content: str = None,
    ):
        self.gmt_created = gmt_created
        self.note_id = note_id
        self.from_official = from_official
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.note_id is not None:
            result['NoteId'] = self.note_id
        if self.from_official is not None:
            result['FromOfficial'] = self.from_official
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')
        if m.get('FromOfficial') is not None:
            self.from_official = m.get('FromOfficial')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ListTicketNotesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListTicketNotesResponseBodyDataList] = None,
    ):
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListTicketNotesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class ListTicketNotesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListTicketNotesResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListTicketNotesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTicketNotesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTicketNotesResponseBody = None,
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
            temp_model = ListTicketNotesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTicketsRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        created_after_time: int = None,
        created_before_time: int = None,
        product_code: str = None,
        page_size: int = None,
        ticket_status: str = None,
        page_start: int = None,
        sub_user_id: str = None,
        language: str = None,
    ):
        self.ids = ids
        self.created_after_time = created_after_time
        self.created_before_time = created_before_time
        self.product_code = product_code
        self.page_size = page_size
        self.ticket_status = ticket_status
        self.page_start = page_start
        self.sub_user_id = sub_user_id
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.created_after_time is not None:
            result['CreatedAfterTime'] = self.created_after_time
        if self.created_before_time is not None:
            result['CreatedBeforeTime'] = self.created_before_time
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ticket_status is not None:
            result['TicketStatus'] = self.ticket_status
        if self.page_start is not None:
            result['PageStart'] = self.page_start
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('CreatedAfterTime') is not None:
            self.created_after_time = m.get('CreatedAfterTime')
        if m.get('CreatedBeforeTime') is not None:
            self.created_before_time = m.get('CreatedBeforeTime')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TicketStatus') is not None:
            self.ticket_status = m.get('TicketStatus')
        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ListTicketsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        ticket_status: str = None,
        title: str = None,
        creator_id: str = None,
        add_time: int = None,
        id: str = None,
    ):
        self.ticket_status = ticket_status
        self.title = title
        self.creator_id = creator_id
        self.add_time = add_time
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ticket_status is not None:
            result['TicketStatus'] = self.ticket_status
        if self.title is not None:
            result['Title'] = self.title
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TicketStatus') is not None:
            self.ticket_status = m.get('TicketStatus')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListTicketsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[ListTicketsResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.list = list
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListTicketsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListTicketsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListTicketsResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListTicketsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTicketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTicketsResponseBody = None,
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
            temp_model = ListTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplyTicketRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        ticket_id: str = None,
        content: str = None,
        secret_content: str = None,
    ):
        self.language = language
        self.ticket_id = ticket_id
        self.content = content
        self.secret_content = secret_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.content is not None:
            result['Content'] = self.content
        if self.secret_content is not None:
            result['SecretContent'] = self.secret_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('SecretContent') is not None:
            self.secret_content = m.get('SecretContent')
        return self


class ReplyTicketResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReplyTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReplyTicketResponseBody = None,
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
            temp_model = ReplyTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


