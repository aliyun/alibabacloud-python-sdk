# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class GetOcCompetitorsRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcCompetitorsResponseBodyData(TeaModel):
    def __init__(
        self,
        competition_brand_introduction: str = None,
        competition_ent_address: str = None,
        competition_ent_es_date: str = None,
        competition_ent_fin_turn: str = None,
        competition_ent_name: str = None,
        competition_introduction: str = None,
        competition_logo_url: str = None,
        competition_product_name: str = None,
        competition_tag: str = None,
        competition_website: str = None,
        ent_name: str = None,
    ):
        self.competition_brand_introduction = competition_brand_introduction
        self.competition_ent_address = competition_ent_address
        self.competition_ent_es_date = competition_ent_es_date
        self.competition_ent_fin_turn = competition_ent_fin_turn
        self.competition_ent_name = competition_ent_name
        self.competition_introduction = competition_introduction
        self.competition_logo_url = competition_logo_url
        self.competition_product_name = competition_product_name
        self.competition_tag = competition_tag
        self.competition_website = competition_website
        self.ent_name = ent_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.competition_brand_introduction is not None:
            result['CompetitionBrandIntroduction'] = self.competition_brand_introduction
        if self.competition_ent_address is not None:
            result['CompetitionEntAddress'] = self.competition_ent_address
        if self.competition_ent_es_date is not None:
            result['CompetitionEntEsDate'] = self.competition_ent_es_date
        if self.competition_ent_fin_turn is not None:
            result['CompetitionEntFinTurn'] = self.competition_ent_fin_turn
        if self.competition_ent_name is not None:
            result['CompetitionEntName'] = self.competition_ent_name
        if self.competition_introduction is not None:
            result['CompetitionIntroduction'] = self.competition_introduction
        if self.competition_logo_url is not None:
            result['CompetitionLogoUrl'] = self.competition_logo_url
        if self.competition_product_name is not None:
            result['CompetitionProductName'] = self.competition_product_name
        if self.competition_tag is not None:
            result['CompetitionTag'] = self.competition_tag
        if self.competition_website is not None:
            result['CompetitionWebsite'] = self.competition_website
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompetitionBrandIntroduction') is not None:
            self.competition_brand_introduction = m.get('CompetitionBrandIntroduction')
        if m.get('CompetitionEntAddress') is not None:
            self.competition_ent_address = m.get('CompetitionEntAddress')
        if m.get('CompetitionEntEsDate') is not None:
            self.competition_ent_es_date = m.get('CompetitionEntEsDate')
        if m.get('CompetitionEntFinTurn') is not None:
            self.competition_ent_fin_turn = m.get('CompetitionEntFinTurn')
        if m.get('CompetitionEntName') is not None:
            self.competition_ent_name = m.get('CompetitionEntName')
        if m.get('CompetitionIntroduction') is not None:
            self.competition_introduction = m.get('CompetitionIntroduction')
        if m.get('CompetitionLogoUrl') is not None:
            self.competition_logo_url = m.get('CompetitionLogoUrl')
        if m.get('CompetitionProductName') is not None:
            self.competition_product_name = m.get('CompetitionProductName')
        if m.get('CompetitionTag') is not None:
            self.competition_tag = m.get('CompetitionTag')
        if m.get('CompetitionWebsite') is not None:
            self.competition_website = m.get('CompetitionWebsite')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        return self


class GetOcCompetitorsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcCompetitorsResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcCompetitorsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcCompetitorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcCompetitorsResponseBody = None,
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
            temp_model = GetOcCompetitorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcCoreTeamsRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcCoreTeamsResponseBodyData(TeaModel):
    def __init__(
        self,
        ent_name: str = None,
        member_introduction: str = None,
        member_name: str = None,
        member_position: str = None,
    ):
        self.ent_name = ent_name
        self.member_introduction = member_introduction
        self.member_name = member_name
        self.member_position = member_position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.member_introduction is not None:
            result['MemberIntroduction'] = self.member_introduction
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.member_position is not None:
            result['MemberPosition'] = self.member_position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('MemberIntroduction') is not None:
            self.member_introduction = m.get('MemberIntroduction')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('MemberPosition') is not None:
            self.member_position = m.get('MemberPosition')
        return self


class GetOcCoreTeamsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcCoreTeamsResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcCoreTeamsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcCoreTeamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcCoreTeamsResponseBody = None,
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
            temp_model = GetOcCoreTeamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcFinancingRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcFinancingResponseBodyData(TeaModel):
    def __init__(
        self,
        ent_name: str = None,
        fin_amount: str = None,
        fin_date: str = None,
        fin_turn: str = None,
        investors: str = None,
    ):
        self.ent_name = ent_name
        self.fin_amount = fin_amount
        self.fin_date = fin_date
        self.fin_turn = fin_turn
        self.investors = investors

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.fin_amount is not None:
            result['FinAmount'] = self.fin_amount
        if self.fin_date is not None:
            result['FinDate'] = self.fin_date
        if self.fin_turn is not None:
            result['FinTurn'] = self.fin_turn
        if self.investors is not None:
            result['Investors'] = self.investors
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('FinAmount') is not None:
            self.fin_amount = m.get('FinAmount')
        if m.get('FinDate') is not None:
            self.fin_date = m.get('FinDate')
        if m.get('FinTurn') is not None:
            self.fin_turn = m.get('FinTurn')
        if m.get('Investors') is not None:
            self.investors = m.get('Investors')
        return self


class GetOcFinancingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcFinancingResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcFinancingResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcFinancingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcFinancingResponseBody = None,
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
            temp_model = GetOcFinancingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcFuzzSearchRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcFuzzSearchResponseBodyData(TeaModel):
    def __init__(
        self,
        ent_name: str = None,
    ):
        self.ent_name = ent_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        return self


class GetOcFuzzSearchResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcFuzzSearchResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcFuzzSearchResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcFuzzSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcFuzzSearchResponseBody = None,
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
            temp_model = GetOcFuzzSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcAbnormalOperationRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcAbnormalOperationResponseBodyData(TeaModel):
    def __init__(
        self,
        in_date: str = None,
        in_department: str = None,
        in_reason: str = None,
        out_date: str = None,
        out_department: str = None,
        out_reason: str = None,
    ):
        self.in_date = in_date
        self.in_department = in_department
        self.in_reason = in_reason
        self.out_date = out_date
        self.out_department = out_department
        self.out_reason = out_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_date is not None:
            result['InDate'] = self.in_date
        if self.in_department is not None:
            result['InDepartment'] = self.in_department
        if self.in_reason is not None:
            result['InReason'] = self.in_reason
        if self.out_date is not None:
            result['OutDate'] = self.out_date
        if self.out_department is not None:
            result['OutDepartment'] = self.out_department
        if self.out_reason is not None:
            result['OutReason'] = self.out_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InDate') is not None:
            self.in_date = m.get('InDate')
        if m.get('InDepartment') is not None:
            self.in_department = m.get('InDepartment')
        if m.get('InReason') is not None:
            self.in_reason = m.get('InReason')
        if m.get('OutDate') is not None:
            self.out_date = m.get('OutDate')
        if m.get('OutDepartment') is not None:
            self.out_department = m.get('OutDepartment')
        if m.get('OutReason') is not None:
            self.out_reason = m.get('OutReason')
        return self


class GetOcIcAbnormalOperationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcAbnormalOperationResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcAbnormalOperationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcAbnormalOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcAbnormalOperationResponseBody = None,
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
            temp_model = GetOcIcAbnormalOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcAdminLicenseRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcAdminLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        department: str = None,
        end_date: str = None,
        license_name: str = None,
        license_no: str = None,
        start_date: str = None,
    ):
        self.content = content
        self.department = department
        self.end_date = end_date
        self.license_name = license_name
        self.license_no = license_no
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.department is not None:
            result['Department'] = self.department
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.license_name is not None:
            result['LicenseName'] = self.license_name
        if self.license_no is not None:
            result['LicenseNo'] = self.license_no
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('LicenseName') is not None:
            self.license_name = m.get('LicenseName')
        if m.get('LicenseNo') is not None:
            self.license_no = m.get('LicenseNo')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetOcIcAdminLicenseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcAdminLicenseResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcAdminLicenseResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcAdminLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcAdminLicenseResponseBody = None,
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
            temp_model = GetOcIcAdminLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcBasicRequest(TeaModel):
    def __init__(
        self,
        search_key: str = None,
    ):
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcBasicResponseBodyData(TeaModel):
    def __init__(
        self,
        check_date: str = None,
        ent_address: str = None,
        ent_brief: str = None,
        ent_name: str = None,
        ent_name_eng: str = None,
        ent_status: str = None,
        ent_type: str = None,
        es_date: str = None,
        former_names: str = None,
        industry_name_lv_1: str = None,
        industry_name_lv_2: str = None,
        insured_num: str = None,
        legal_name: str = None,
        license_number: str = None,
        op_from: str = None,
        op_scope: str = None,
        op_to: str = None,
        org_no: str = None,
        rec_cap: str = None,
        reg_cap: str = None,
        reg_org: str = None,
        reg_org_city: str = None,
        reg_org_district: str = None,
        reg_org_province: str = None,
        social_credit_code: str = None,
        staff_num: str = None,
        tax_num: str = None,
    ):
        self.check_date = check_date
        self.ent_address = ent_address
        self.ent_brief = ent_brief
        self.ent_name = ent_name
        self.ent_name_eng = ent_name_eng
        self.ent_status = ent_status
        self.ent_type = ent_type
        self.es_date = es_date
        self.former_names = former_names
        self.industry_name_lv_1 = industry_name_lv_1
        self.industry_name_lv_2 = industry_name_lv_2
        self.insured_num = insured_num
        self.legal_name = legal_name
        self.license_number = license_number
        self.op_from = op_from
        self.op_scope = op_scope
        self.op_to = op_to
        self.org_no = org_no
        self.rec_cap = rec_cap
        self.reg_cap = reg_cap
        self.reg_org = reg_org
        self.reg_org_city = reg_org_city
        self.reg_org_district = reg_org_district
        self.reg_org_province = reg_org_province
        self.social_credit_code = social_credit_code
        self.staff_num = staff_num
        self.tax_num = tax_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_date is not None:
            result['CheckDate'] = self.check_date
        if self.ent_address is not None:
            result['EntAddress'] = self.ent_address
        if self.ent_brief is not None:
            result['EntBrief'] = self.ent_brief
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.ent_name_eng is not None:
            result['EntNameEng'] = self.ent_name_eng
        if self.ent_status is not None:
            result['EntStatus'] = self.ent_status
        if self.ent_type is not None:
            result['EntType'] = self.ent_type
        if self.es_date is not None:
            result['EsDate'] = self.es_date
        if self.former_names is not None:
            result['FormerNames'] = self.former_names
        if self.industry_name_lv_1 is not None:
            result['IndustryNameLv1'] = self.industry_name_lv_1
        if self.industry_name_lv_2 is not None:
            result['IndustryNameLv2'] = self.industry_name_lv_2
        if self.insured_num is not None:
            result['InsuredNum'] = self.insured_num
        if self.legal_name is not None:
            result['LegalName'] = self.legal_name
        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number
        if self.op_from is not None:
            result['OpFrom'] = self.op_from
        if self.op_scope is not None:
            result['OpScope'] = self.op_scope
        if self.op_to is not None:
            result['OpTo'] = self.op_to
        if self.org_no is not None:
            result['OrgNo'] = self.org_no
        if self.rec_cap is not None:
            result['RecCap'] = self.rec_cap
        if self.reg_cap is not None:
            result['RegCap'] = self.reg_cap
        if self.reg_org is not None:
            result['RegOrg'] = self.reg_org
        if self.reg_org_city is not None:
            result['RegOrgCity'] = self.reg_org_city
        if self.reg_org_district is not None:
            result['RegOrgDistrict'] = self.reg_org_district
        if self.reg_org_province is not None:
            result['RegOrgProvince'] = self.reg_org_province
        if self.social_credit_code is not None:
            result['SocialCreditCode'] = self.social_credit_code
        if self.staff_num is not None:
            result['StaffNum'] = self.staff_num
        if self.tax_num is not None:
            result['TaxNum'] = self.tax_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckDate') is not None:
            self.check_date = m.get('CheckDate')
        if m.get('EntAddress') is not None:
            self.ent_address = m.get('EntAddress')
        if m.get('EntBrief') is not None:
            self.ent_brief = m.get('EntBrief')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('EntNameEng') is not None:
            self.ent_name_eng = m.get('EntNameEng')
        if m.get('EntStatus') is not None:
            self.ent_status = m.get('EntStatus')
        if m.get('EntType') is not None:
            self.ent_type = m.get('EntType')
        if m.get('EsDate') is not None:
            self.es_date = m.get('EsDate')
        if m.get('FormerNames') is not None:
            self.former_names = m.get('FormerNames')
        if m.get('IndustryNameLv1') is not None:
            self.industry_name_lv_1 = m.get('IndustryNameLv1')
        if m.get('IndustryNameLv2') is not None:
            self.industry_name_lv_2 = m.get('IndustryNameLv2')
        if m.get('InsuredNum') is not None:
            self.insured_num = m.get('InsuredNum')
        if m.get('LegalName') is not None:
            self.legal_name = m.get('LegalName')
        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')
        if m.get('OpFrom') is not None:
            self.op_from = m.get('OpFrom')
        if m.get('OpScope') is not None:
            self.op_scope = m.get('OpScope')
        if m.get('OpTo') is not None:
            self.op_to = m.get('OpTo')
        if m.get('OrgNo') is not None:
            self.org_no = m.get('OrgNo')
        if m.get('RecCap') is not None:
            self.rec_cap = m.get('RecCap')
        if m.get('RegCap') is not None:
            self.reg_cap = m.get('RegCap')
        if m.get('RegOrg') is not None:
            self.reg_org = m.get('RegOrg')
        if m.get('RegOrgCity') is not None:
            self.reg_org_city = m.get('RegOrgCity')
        if m.get('RegOrgDistrict') is not None:
            self.reg_org_district = m.get('RegOrgDistrict')
        if m.get('RegOrgProvince') is not None:
            self.reg_org_province = m.get('RegOrgProvince')
        if m.get('SocialCreditCode') is not None:
            self.social_credit_code = m.get('SocialCreditCode')
        if m.get('StaffNum') is not None:
            self.staff_num = m.get('StaffNum')
        if m.get('TaxNum') is not None:
            self.tax_num = m.get('TaxNum')
        return self


class GetOcIcBasicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetOcIcBasicResponseBodyData = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

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
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetOcIcBasicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcBasicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcBasicResponseBody = None,
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
            temp_model = GetOcIcBasicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcBranchRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcBranchResponseBodyData(TeaModel):
    def __init__(
        self,
        ent_name: str = None,
        ent_status: str = None,
        es_date: str = None,
        oper_name: str = None,
    ):
        self.ent_name = ent_name
        self.ent_status = ent_status
        self.es_date = es_date
        self.oper_name = oper_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.ent_status is not None:
            result['EntStatus'] = self.ent_status
        if self.es_date is not None:
            result['EsDate'] = self.es_date
        if self.oper_name is not None:
            result['OperName'] = self.oper_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('EntStatus') is not None:
            self.ent_status = m.get('EntStatus')
        if m.get('EsDate') is not None:
            self.es_date = m.get('EsDate')
        if m.get('OperName') is not None:
            self.oper_name = m.get('OperName')
        return self


class GetOcIcBranchResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcBranchResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcBranchResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcBranchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcBranchResponseBody = None,
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
            temp_model = GetOcIcBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcChangeRecordRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcChangeRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        after_content: str = None,
        before_content: str = None,
        change_date: str = None,
        type: str = None,
    ):
        self.after_content = after_content
        self.before_content = before_content
        self.change_date = change_date
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_content is not None:
            result['AfterContent'] = self.after_content
        if self.before_content is not None:
            result['BeforeContent'] = self.before_content
        if self.change_date is not None:
            result['ChangeDate'] = self.change_date
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterContent') is not None:
            self.after_content = m.get('AfterContent')
        if m.get('BeforeContent') is not None:
            self.before_content = m.get('BeforeContent')
        if m.get('ChangeDate') is not None:
            self.change_date = m.get('ChangeDate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetOcIcChangeRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcChangeRecordResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcChangeRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcChangeRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcChangeRecordResponseBody = None,
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
            temp_model = GetOcIcChangeRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcCheckupRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcCheckupResponseBodyData(TeaModel):
    def __init__(
        self,
        date: str = None,
        department: str = None,
        result: str = None,
        type: str = None,
    ):
        self.date = date
        self.department = department
        self.result = result
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.department is not None:
            result['Department'] = self.department
        if self.result is not None:
            result['Result'] = self.result
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetOcIcCheckupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcCheckupResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcCheckupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcCheckupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcCheckupResponseBody = None,
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
            temp_model = GetOcIcCheckupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcClearAccountRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcClearAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        leader: str = None,
        member: str = None,
    ):
        self.leader = leader
        self.member = member

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.leader is not None:
            result['Leader'] = self.leader
        if self.member is not None:
            result['Member'] = self.member
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Leader') is not None:
            self.leader = m.get('Leader')
        if m.get('Member') is not None:
            self.member = m.get('Member')
        return self


class GetOcIcClearAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcClearAccountResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcClearAccountResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcClearAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcClearAccountResponseBody = None,
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
            temp_model = GetOcIcClearAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcDoubleCheckupRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcDoubleCheckupResponseBodyData(TeaModel):
    def __init__(
        self,
        inspect_date: str = None,
        inspect_department: str = None,
        inspect_item: str = None,
        inspect_plan_id: str = None,
        inspect_plan_name: str = None,
        inspect_result: str = None,
        inspect_task_id: str = None,
        inspect_task_name: str = None,
        inspect_type_name: str = None,
    ):
        self.inspect_date = inspect_date
        self.inspect_department = inspect_department
        self.inspect_item = inspect_item
        self.inspect_plan_id = inspect_plan_id
        self.inspect_plan_name = inspect_plan_name
        self.inspect_result = inspect_result
        self.inspect_task_id = inspect_task_id
        self.inspect_task_name = inspect_task_name
        self.inspect_type_name = inspect_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspect_date is not None:
            result['InspectDate'] = self.inspect_date
        if self.inspect_department is not None:
            result['InspectDepartment'] = self.inspect_department
        if self.inspect_item is not None:
            result['InspectItem'] = self.inspect_item
        if self.inspect_plan_id is not None:
            result['InspectPlanId'] = self.inspect_plan_id
        if self.inspect_plan_name is not None:
            result['InspectPlanName'] = self.inspect_plan_name
        if self.inspect_result is not None:
            result['InspectResult'] = self.inspect_result
        if self.inspect_task_id is not None:
            result['InspectTaskId'] = self.inspect_task_id
        if self.inspect_task_name is not None:
            result['InspectTaskName'] = self.inspect_task_name
        if self.inspect_type_name is not None:
            result['InspectTypeName'] = self.inspect_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectDate') is not None:
            self.inspect_date = m.get('InspectDate')
        if m.get('InspectDepartment') is not None:
            self.inspect_department = m.get('InspectDepartment')
        if m.get('InspectItem') is not None:
            self.inspect_item = m.get('InspectItem')
        if m.get('InspectPlanId') is not None:
            self.inspect_plan_id = m.get('InspectPlanId')
        if m.get('InspectPlanName') is not None:
            self.inspect_plan_name = m.get('InspectPlanName')
        if m.get('InspectResult') is not None:
            self.inspect_result = m.get('InspectResult')
        if m.get('InspectTaskId') is not None:
            self.inspect_task_id = m.get('InspectTaskId')
        if m.get('InspectTaskName') is not None:
            self.inspect_task_name = m.get('InspectTaskName')
        if m.get('InspectTypeName') is not None:
            self.inspect_type_name = m.get('InspectTypeName')
        return self


class GetOcIcDoubleCheckupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcDoubleCheckupResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcDoubleCheckupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcDoubleCheckupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcDoubleCheckupResponseBody = None,
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
            temp_model = GetOcIcDoubleCheckupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcEmployeeRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcEmployeeResponseBodyData(TeaModel):
    def __init__(
        self,
        job_title: str = None,
        name: str = None,
    ):
        self.job_title = job_title
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_title is not None:
            result['JobTitle'] = self.job_title
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobTitle') is not None:
            self.job_title = m.get('JobTitle')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetOcIcEmployeeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcEmployeeResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcEmployeeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcEmployeeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcEmployeeResponseBody = None,
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
            temp_model = GetOcIcEmployeeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcEquityFrozenRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcEquityFrozenResponseBodyData(TeaModel):
    def __init__(
        self,
        freeze_amount: str = None,
        freeze_card_num: str = None,
        freeze_card_type: str = None,
        freeze_court: str = None,
        freeze_end_date: str = None,
        freeze_exec_item: str = None,
        freeze_exec_person: str = None,
        freeze_notice_num: str = None,
        freeze_publish_date: str = None,
        freeze_start_date: str = None,
        status: str = None,
        unfreeze_adjust_num: str = None,
        unfreeze_court: str = None,
        unfreeze_date: str = None,
        unfreeze_reason: str = None,
    ):
        self.freeze_amount = freeze_amount
        self.freeze_card_num = freeze_card_num
        self.freeze_card_type = freeze_card_type
        self.freeze_court = freeze_court
        self.freeze_end_date = freeze_end_date
        self.freeze_exec_item = freeze_exec_item
        self.freeze_exec_person = freeze_exec_person
        self.freeze_notice_num = freeze_notice_num
        self.freeze_publish_date = freeze_publish_date
        self.freeze_start_date = freeze_start_date
        self.status = status
        self.unfreeze_adjust_num = unfreeze_adjust_num
        self.unfreeze_court = unfreeze_court
        self.unfreeze_date = unfreeze_date
        self.unfreeze_reason = unfreeze_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.freeze_amount is not None:
            result['FreezeAmount'] = self.freeze_amount
        if self.freeze_card_num is not None:
            result['FreezeCardNum'] = self.freeze_card_num
        if self.freeze_card_type is not None:
            result['FreezeCardType'] = self.freeze_card_type
        if self.freeze_court is not None:
            result['FreezeCourt'] = self.freeze_court
        if self.freeze_end_date is not None:
            result['FreezeEndDate'] = self.freeze_end_date
        if self.freeze_exec_item is not None:
            result['FreezeExecItem'] = self.freeze_exec_item
        if self.freeze_exec_person is not None:
            result['FreezeExecPerson'] = self.freeze_exec_person
        if self.freeze_notice_num is not None:
            result['FreezeNoticeNum'] = self.freeze_notice_num
        if self.freeze_publish_date is not None:
            result['FreezePublishDate'] = self.freeze_publish_date
        if self.freeze_start_date is not None:
            result['FreezeStartDate'] = self.freeze_start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.unfreeze_adjust_num is not None:
            result['UnfreezeAdjustNum'] = self.unfreeze_adjust_num
        if self.unfreeze_court is not None:
            result['UnfreezeCourt'] = self.unfreeze_court
        if self.unfreeze_date is not None:
            result['UnfreezeDate'] = self.unfreeze_date
        if self.unfreeze_reason is not None:
            result['UnfreezeReason'] = self.unfreeze_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreezeAmount') is not None:
            self.freeze_amount = m.get('FreezeAmount')
        if m.get('FreezeCardNum') is not None:
            self.freeze_card_num = m.get('FreezeCardNum')
        if m.get('FreezeCardType') is not None:
            self.freeze_card_type = m.get('FreezeCardType')
        if m.get('FreezeCourt') is not None:
            self.freeze_court = m.get('FreezeCourt')
        if m.get('FreezeEndDate') is not None:
            self.freeze_end_date = m.get('FreezeEndDate')
        if m.get('FreezeExecItem') is not None:
            self.freeze_exec_item = m.get('FreezeExecItem')
        if m.get('FreezeExecPerson') is not None:
            self.freeze_exec_person = m.get('FreezeExecPerson')
        if m.get('FreezeNoticeNum') is not None:
            self.freeze_notice_num = m.get('FreezeNoticeNum')
        if m.get('FreezePublishDate') is not None:
            self.freeze_publish_date = m.get('FreezePublishDate')
        if m.get('FreezeStartDate') is not None:
            self.freeze_start_date = m.get('FreezeStartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnfreezeAdjustNum') is not None:
            self.unfreeze_adjust_num = m.get('UnfreezeAdjustNum')
        if m.get('UnfreezeCourt') is not None:
            self.unfreeze_court = m.get('UnfreezeCourt')
        if m.get('UnfreezeDate') is not None:
            self.unfreeze_date = m.get('UnfreezeDate')
        if m.get('UnfreezeReason') is not None:
            self.unfreeze_reason = m.get('UnfreezeReason')
        return self


class GetOcIcEquityFrozenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcEquityFrozenResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcEquityFrozenResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcEquityFrozenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcEquityFrozenResponseBody = None,
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
            temp_model = GetOcIcEquityFrozenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcEquityPledgeRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcEquityPledgeResponseBodyData(TeaModel):
    def __init__(
        self,
        number: str = None,
        pawnee: str = None,
        pawnee_identify_no: str = None,
        pledgor: str = None,
        pledgor_amount: str = None,
        pledgor_identify_no: str = None,
        public_date: str = None,
        reg_date: str = None,
        related_comp: str = None,
        status: str = None,
    ):
        self.number = number
        self.pawnee = pawnee
        self.pawnee_identify_no = pawnee_identify_no
        self.pledgor = pledgor
        self.pledgor_amount = pledgor_amount
        self.pledgor_identify_no = pledgor_identify_no
        self.public_date = public_date
        self.reg_date = reg_date
        self.related_comp = related_comp
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.pawnee is not None:
            result['Pawnee'] = self.pawnee
        if self.pawnee_identify_no is not None:
            result['PawneeIdentifyNo'] = self.pawnee_identify_no
        if self.pledgor is not None:
            result['Pledgor'] = self.pledgor
        if self.pledgor_amount is not None:
            result['PledgorAmount'] = self.pledgor_amount
        if self.pledgor_identify_no is not None:
            result['PledgorIdentifyNo'] = self.pledgor_identify_no
        if self.public_date is not None:
            result['PublicDate'] = self.public_date
        if self.reg_date is not None:
            result['RegDate'] = self.reg_date
        if self.related_comp is not None:
            result['RelatedComp'] = self.related_comp
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Pawnee') is not None:
            self.pawnee = m.get('Pawnee')
        if m.get('PawneeIdentifyNo') is not None:
            self.pawnee_identify_no = m.get('PawneeIdentifyNo')
        if m.get('Pledgor') is not None:
            self.pledgor = m.get('Pledgor')
        if m.get('PledgorAmount') is not None:
            self.pledgor_amount = m.get('PledgorAmount')
        if m.get('PledgorIdentifyNo') is not None:
            self.pledgor_identify_no = m.get('PledgorIdentifyNo')
        if m.get('PublicDate') is not None:
            self.public_date = m.get('PublicDate')
        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')
        if m.get('RelatedComp') is not None:
            self.related_comp = m.get('RelatedComp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetOcIcEquityPledgeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcEquityPledgeResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcEquityPledgeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcEquityPledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcEquityPledgeResponseBody = None,
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
            temp_model = GetOcIcEquityPledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcInvestmentRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcInvestmentResponseBodyData(TeaModel):
    def __init__(
        self,
        ent_name: str = None,
        invest_credit_code: str = None,
        invest_es_date: str = None,
        invest_legal_name: str = None,
        invest_license_no: str = None,
        invest_name: str = None,
        invest_reg_cap: str = None,
        invest_status: str = None,
        should_cap: str = None,
        stock_percentage: str = None,
    ):
        self.ent_name = ent_name
        self.invest_credit_code = invest_credit_code
        self.invest_es_date = invest_es_date
        self.invest_legal_name = invest_legal_name
        self.invest_license_no = invest_license_no
        self.invest_name = invest_name
        self.invest_reg_cap = invest_reg_cap
        self.invest_status = invest_status
        self.should_cap = should_cap
        self.stock_percentage = stock_percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.invest_credit_code is not None:
            result['InvestCreditCode'] = self.invest_credit_code
        if self.invest_es_date is not None:
            result['InvestEsDate'] = self.invest_es_date
        if self.invest_legal_name is not None:
            result['InvestLegalName'] = self.invest_legal_name
        if self.invest_license_no is not None:
            result['InvestLicenseNo'] = self.invest_license_no
        if self.invest_name is not None:
            result['InvestName'] = self.invest_name
        if self.invest_reg_cap is not None:
            result['InvestRegCap'] = self.invest_reg_cap
        if self.invest_status is not None:
            result['InvestStatus'] = self.invest_status
        if self.should_cap is not None:
            result['ShouldCap'] = self.should_cap
        if self.stock_percentage is not None:
            result['StockPercentage'] = self.stock_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('InvestCreditCode') is not None:
            self.invest_credit_code = m.get('InvestCreditCode')
        if m.get('InvestEsDate') is not None:
            self.invest_es_date = m.get('InvestEsDate')
        if m.get('InvestLegalName') is not None:
            self.invest_legal_name = m.get('InvestLegalName')
        if m.get('InvestLicenseNo') is not None:
            self.invest_license_no = m.get('InvestLicenseNo')
        if m.get('InvestName') is not None:
            self.invest_name = m.get('InvestName')
        if m.get('InvestRegCap') is not None:
            self.invest_reg_cap = m.get('InvestRegCap')
        if m.get('InvestStatus') is not None:
            self.invest_status = m.get('InvestStatus')
        if m.get('ShouldCap') is not None:
            self.should_cap = m.get('ShouldCap')
        if m.get('StockPercentage') is not None:
            self.stock_percentage = m.get('StockPercentage')
        return self


class GetOcIcInvestmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcInvestmentResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcInvestmentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcInvestmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcInvestmentResponseBody = None,
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
            temp_model = GetOcIcInvestmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcKnowledgePropertyPledgeRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcKnowledgePropertyPledgeResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        number: str = None,
        pawnee: str = None,
        period: str = None,
        pledgor: str = None,
        public_date: str = None,
        status: str = None,
        type: str = None,
    ):
        self.name = name
        self.number = number
        self.pawnee = pawnee
        self.period = period
        self.pledgor = pledgor
        self.public_date = public_date
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.pawnee is not None:
            result['Pawnee'] = self.pawnee
        if self.period is not None:
            result['Period'] = self.period
        if self.pledgor is not None:
            result['Pledgor'] = self.pledgor
        if self.public_date is not None:
            result['PublicDate'] = self.public_date
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Pawnee') is not None:
            self.pawnee = m.get('Pawnee')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Pledgor') is not None:
            self.pledgor = m.get('Pledgor')
        if m.get('PublicDate') is not None:
            self.public_date = m.get('PublicDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetOcIcKnowledgePropertyPledgeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcKnowledgePropertyPledgeResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcKnowledgePropertyPledgeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcKnowledgePropertyPledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcKnowledgePropertyPledgeResponseBody = None,
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
            temp_model = GetOcIcKnowledgePropertyPledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcMortgageRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcMortgageResponseBodyData(TeaModel):
    def __init__(
        self,
        debit_amount: str = None,
        debit_period: str = None,
        debit_scope: str = None,
        debit_type: str = None,
        department: str = None,
        guarantees: str = None,
        identify_no: str = None,
        identify_type: str = None,
        mortgagees_name: str = None,
        number: str = None,
        onecomp_id: str = None,
        public_date: str = None,
        reg_date: str = None,
        status: str = None,
    ):
        self.debit_amount = debit_amount
        self.debit_period = debit_period
        self.debit_scope = debit_scope
        self.debit_type = debit_type
        self.department = department
        self.guarantees = guarantees
        self.identify_no = identify_no
        self.identify_type = identify_type
        self.mortgagees_name = mortgagees_name
        self.number = number
        # ocid
        self.onecomp_id = onecomp_id
        self.public_date = public_date
        self.reg_date = reg_date
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debit_amount is not None:
            result['DebitAmount'] = self.debit_amount
        if self.debit_period is not None:
            result['DebitPeriod'] = self.debit_period
        if self.debit_scope is not None:
            result['DebitScope'] = self.debit_scope
        if self.debit_type is not None:
            result['DebitType'] = self.debit_type
        if self.department is not None:
            result['Department'] = self.department
        if self.guarantees is not None:
            result['Guarantees'] = self.guarantees
        if self.identify_no is not None:
            result['IdentifyNo'] = self.identify_no
        if self.identify_type is not None:
            result['IdentifyType'] = self.identify_type
        if self.mortgagees_name is not None:
            result['MortgageesName'] = self.mortgagees_name
        if self.number is not None:
            result['Number'] = self.number
        if self.onecomp_id is not None:
            result['OnecompId'] = self.onecomp_id
        if self.public_date is not None:
            result['PublicDate'] = self.public_date
        if self.reg_date is not None:
            result['RegDate'] = self.reg_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebitAmount') is not None:
            self.debit_amount = m.get('DebitAmount')
        if m.get('DebitPeriod') is not None:
            self.debit_period = m.get('DebitPeriod')
        if m.get('DebitScope') is not None:
            self.debit_scope = m.get('DebitScope')
        if m.get('DebitType') is not None:
            self.debit_type = m.get('DebitType')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('Guarantees') is not None:
            self.guarantees = m.get('Guarantees')
        if m.get('IdentifyNo') is not None:
            self.identify_no = m.get('IdentifyNo')
        if m.get('IdentifyType') is not None:
            self.identify_type = m.get('IdentifyType')
        if m.get('MortgageesName') is not None:
            self.mortgagees_name = m.get('MortgageesName')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OnecompId') is not None:
            self.onecomp_id = m.get('OnecompId')
        if m.get('PublicDate') is not None:
            self.public_date = m.get('PublicDate')
        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetOcIcMortgageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcMortgageResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcMortgageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcMortgageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcMortgageResponseBody = None,
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
            temp_model = GetOcIcMortgageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcSeriousOffenseRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcSeriousOffenseResponseBodyData(TeaModel):
    def __init__(
        self,
        ent_name: str = None,
        in_date: str = None,
        in_department: str = None,
        in_reason: str = None,
        out_date: str = None,
        out_department: str = None,
        out_reason: str = None,
    ):
        self.ent_name = ent_name
        self.in_date = in_date
        self.in_department = in_department
        self.in_reason = in_reason
        self.out_date = out_date
        self.out_department = out_department
        self.out_reason = out_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.in_date is not None:
            result['InDate'] = self.in_date
        if self.in_department is not None:
            result['InDepartment'] = self.in_department
        if self.in_reason is not None:
            result['InReason'] = self.in_reason
        if self.out_date is not None:
            result['OutDate'] = self.out_date
        if self.out_department is not None:
            result['OutDepartment'] = self.out_department
        if self.out_reason is not None:
            result['OutReason'] = self.out_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('InDate') is not None:
            self.in_date = m.get('InDate')
        if m.get('InDepartment') is not None:
            self.in_department = m.get('InDepartment')
        if m.get('InReason') is not None:
            self.in_reason = m.get('InReason')
        if m.get('OutDate') is not None:
            self.out_date = m.get('OutDate')
        if m.get('OutDepartment') is not None:
            self.out_department = m.get('OutDepartment')
        if m.get('OutReason') is not None:
            self.out_reason = m.get('OutReason')
        return self


class GetOcIcSeriousOffenseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcSeriousOffenseResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcSeriousOffenseResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcSeriousOffenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcSeriousOffenseResponseBody = None,
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
            temp_model = GetOcIcSeriousOffenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcShareholderRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcShareholderResponseBodyData(TeaModel):
    def __init__(
        self,
        should_cap: str = None,
        should_cap_time: str = None,
        stock_name: str = None,
        stock_percent: str = None,
        stock_type: str = None,
    ):
        self.should_cap = should_cap
        self.should_cap_time = should_cap_time
        self.stock_name = stock_name
        self.stock_percent = stock_percent
        self.stock_type = stock_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.should_cap is not None:
            result['ShouldCap'] = self.should_cap
        if self.should_cap_time is not None:
            result['ShouldCapTime'] = self.should_cap_time
        if self.stock_name is not None:
            result['StockName'] = self.stock_name
        if self.stock_percent is not None:
            result['StockPercent'] = self.stock_percent
        if self.stock_type is not None:
            result['StockType'] = self.stock_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShouldCap') is not None:
            self.should_cap = m.get('ShouldCap')
        if m.get('ShouldCapTime') is not None:
            self.should_cap_time = m.get('ShouldCapTime')
        if m.get('StockName') is not None:
            self.stock_name = m.get('StockName')
        if m.get('StockPercent') is not None:
            self.stock_percent = m.get('StockPercent')
        if m.get('StockType') is not None:
            self.stock_type = m.get('StockType')
        return self


class GetOcIcShareholderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcShareholderResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcShareholderResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcShareholderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcShareholderResponseBody = None,
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
            temp_model = GetOcIcShareholderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIcSimpleCancelRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIcSimpleCancelResponseBodyData(TeaModel):
    def __init__(
        self,
        department: str = None,
        ent_name: str = None,
        notice_period: str = None,
        sca_content: str = None,
        sca_date: str = None,
        sca_proposer: str = None,
        sca_result: str = None,
        sca_result_date: str = None,
        social_credit_code: str = None,
    ):
        self.department = department
        self.ent_name = ent_name
        self.notice_period = notice_period
        self.sca_content = sca_content
        self.sca_date = sca_date
        self.sca_proposer = sca_proposer
        self.sca_result = sca_result
        self.sca_result_date = sca_result_date
        self.social_credit_code = social_credit_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department is not None:
            result['Department'] = self.department
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.notice_period is not None:
            result['NoticePeriod'] = self.notice_period
        if self.sca_content is not None:
            result['ScaContent'] = self.sca_content
        if self.sca_date is not None:
            result['ScaDate'] = self.sca_date
        if self.sca_proposer is not None:
            result['ScaProposer'] = self.sca_proposer
        if self.sca_result is not None:
            result['ScaResult'] = self.sca_result
        if self.sca_result_date is not None:
            result['ScaResultDate'] = self.sca_result_date
        if self.social_credit_code is not None:
            result['SocialCreditCode'] = self.social_credit_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('NoticePeriod') is not None:
            self.notice_period = m.get('NoticePeriod')
        if m.get('ScaContent') is not None:
            self.sca_content = m.get('ScaContent')
        if m.get('ScaDate') is not None:
            self.sca_date = m.get('ScaDate')
        if m.get('ScaProposer') is not None:
            self.sca_proposer = m.get('ScaProposer')
        if m.get('ScaResult') is not None:
            self.sca_result = m.get('ScaResult')
        if m.get('ScaResultDate') is not None:
            self.sca_result_date = m.get('ScaResultDate')
        if m.get('SocialCreditCode') is not None:
            self.social_credit_code = m.get('SocialCreditCode')
        return self


class GetOcIcSimpleCancelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIcSimpleCancelResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIcSimpleCancelResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIcSimpleCancelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIcSimpleCancelResponseBody = None,
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
            temp_model = GetOcIcSimpleCancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIpCertificateRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIpCertificateResponseBodyData(TeaModel):
    def __init__(
        self,
        authorize_date: str = None,
        authorize_department: str = None,
        cert_num: str = None,
        cert_scope: str = None,
        cert_type: str = None,
        ent_name: str = None,
        province: str = None,
        pub_date: str = None,
        valid_end_date: str = None,
        valid_start_date: str = None,
    ):
        self.authorize_date = authorize_date
        self.authorize_department = authorize_department
        self.cert_num = cert_num
        self.cert_scope = cert_scope
        self.cert_type = cert_type
        self.ent_name = ent_name
        self.province = province
        self.pub_date = pub_date
        self.valid_end_date = valid_end_date
        self.valid_start_date = valid_start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize_date is not None:
            result['AuthorizeDate'] = self.authorize_date
        if self.authorize_department is not None:
            result['AuthorizeDepartment'] = self.authorize_department
        if self.cert_num is not None:
            result['CertNum'] = self.cert_num
        if self.cert_scope is not None:
            result['CertScope'] = self.cert_scope
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.province is not None:
            result['Province'] = self.province
        if self.pub_date is not None:
            result['PubDate'] = self.pub_date
        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date
        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizeDate') is not None:
            self.authorize_date = m.get('AuthorizeDate')
        if m.get('AuthorizeDepartment') is not None:
            self.authorize_department = m.get('AuthorizeDepartment')
        if m.get('CertNum') is not None:
            self.cert_num = m.get('CertNum')
        if m.get('CertScope') is not None:
            self.cert_scope = m.get('CertScope')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('PubDate') is not None:
            self.pub_date = m.get('PubDate')
        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')
        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')
        return self


class GetOcIpCertificateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIpCertificateResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIpCertificateResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIpCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIpCertificateResponseBody = None,
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
            temp_model = GetOcIpCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIpDomainRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIpDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        check_date: str = None,
        domain: str = None,
        ent_name: str = None,
        home_url: str = None,
        number: str = None,
        site_name: str = None,
    ):
        self.check_date = check_date
        self.domain = domain
        self.ent_name = ent_name
        self.home_url = home_url
        self.number = number
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_date is not None:
            result['CheckDate'] = self.check_date
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.home_url is not None:
            result['HomeUrl'] = self.home_url
        if self.number is not None:
            result['Number'] = self.number
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckDate') is not None:
            self.check_date = m.get('CheckDate')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('HomeUrl') is not None:
            self.home_url = m.get('HomeUrl')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        return self


class GetOcIpDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIpDomainResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIpDomainResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIpDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIpDomainResponseBody = None,
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
            temp_model = GetOcIpDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIpPatentRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIpPatentResponseBodyData(TeaModel):
    def __init__(
        self,
        agency: str = None,
        agent: str = None,
        brief: str = None,
        cate_num: str = None,
        ent_name: str = None,
        inventor_list: str = None,
        main_claim: str = None,
        patent_name: str = None,
        patent_status: str = None,
        patent_type: str = None,
        patentee_list: str = None,
        prio_date: str = None,
        prio_num: str = None,
        public_date: str = None,
        public_num: str = None,
        request_date: str = None,
        request_num: str = None,
    ):
        self.agency = agency
        self.agent = agent
        self.brief = brief
        self.cate_num = cate_num
        self.ent_name = ent_name
        self.inventor_list = inventor_list
        self.main_claim = main_claim
        self.patent_name = patent_name
        self.patent_status = patent_status
        self.patent_type = patent_type
        self.patentee_list = patentee_list
        self.prio_date = prio_date
        self.prio_num = prio_num
        self.public_date = public_date
        self.public_num = public_num
        self.request_date = request_date
        self.request_num = request_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agency is not None:
            result['Agency'] = self.agency
        if self.agent is not None:
            result['Agent'] = self.agent
        if self.brief is not None:
            result['Brief'] = self.brief
        if self.cate_num is not None:
            result['CateNum'] = self.cate_num
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.inventor_list is not None:
            result['InventorList'] = self.inventor_list
        if self.main_claim is not None:
            result['MainClaim'] = self.main_claim
        if self.patent_name is not None:
            result['PatentName'] = self.patent_name
        if self.patent_status is not None:
            result['PatentStatus'] = self.patent_status
        if self.patent_type is not None:
            result['PatentType'] = self.patent_type
        if self.patentee_list is not None:
            result['PatenteeList'] = self.patentee_list
        if self.prio_date is not None:
            result['PrioDate'] = self.prio_date
        if self.prio_num is not None:
            result['PrioNum'] = self.prio_num
        if self.public_date is not None:
            result['PublicDate'] = self.public_date
        if self.public_num is not None:
            result['PublicNum'] = self.public_num
        if self.request_date is not None:
            result['RequestDate'] = self.request_date
        if self.request_num is not None:
            result['RequestNum'] = self.request_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agency') is not None:
            self.agency = m.get('Agency')
        if m.get('Agent') is not None:
            self.agent = m.get('Agent')
        if m.get('Brief') is not None:
            self.brief = m.get('Brief')
        if m.get('CateNum') is not None:
            self.cate_num = m.get('CateNum')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('InventorList') is not None:
            self.inventor_list = m.get('InventorList')
        if m.get('MainClaim') is not None:
            self.main_claim = m.get('MainClaim')
        if m.get('PatentName') is not None:
            self.patent_name = m.get('PatentName')
        if m.get('PatentStatus') is not None:
            self.patent_status = m.get('PatentStatus')
        if m.get('PatentType') is not None:
            self.patent_type = m.get('PatentType')
        if m.get('PatenteeList') is not None:
            self.patentee_list = m.get('PatenteeList')
        if m.get('PrioDate') is not None:
            self.prio_date = m.get('PrioDate')
        if m.get('PrioNum') is not None:
            self.prio_num = m.get('PrioNum')
        if m.get('PublicDate') is not None:
            self.public_date = m.get('PublicDate')
        if m.get('PublicNum') is not None:
            self.public_num = m.get('PublicNum')
        if m.get('RequestDate') is not None:
            self.request_date = m.get('RequestDate')
        if m.get('RequestNum') is not None:
            self.request_num = m.get('RequestNum')
        return self


class GetOcIpPatentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIpPatentResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIpPatentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIpPatentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIpPatentResponseBody = None,
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
            temp_model = GetOcIpPatentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIpSoftwareCopyrightRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIpSoftwareCopyrightResponseBodyData(TeaModel):
    def __init__(
        self,
        approval_date: str = None,
        copy_name: str = None,
        copy_num: str = None,
        ent_name: str = None,
        first_date: str = None,
        short_name: str = None,
        success_date: str = None,
        type_num: str = None,
        version: str = None,
    ):
        self.approval_date = approval_date
        self.copy_name = copy_name
        self.copy_num = copy_num
        self.ent_name = ent_name
        self.first_date = first_date
        self.short_name = short_name
        self.success_date = success_date
        self.type_num = type_num
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_date is not None:
            result['ApprovalDate'] = self.approval_date
        if self.copy_name is not None:
            result['CopyName'] = self.copy_name
        if self.copy_num is not None:
            result['CopyNum'] = self.copy_num
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.first_date is not None:
            result['FirstDate'] = self.first_date
        if self.short_name is not None:
            result['ShortName'] = self.short_name
        if self.success_date is not None:
            result['SuccessDate'] = self.success_date
        if self.type_num is not None:
            result['TypeNum'] = self.type_num
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalDate') is not None:
            self.approval_date = m.get('ApprovalDate')
        if m.get('CopyName') is not None:
            self.copy_name = m.get('CopyName')
        if m.get('CopyNum') is not None:
            self.copy_num = m.get('CopyNum')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('FirstDate') is not None:
            self.first_date = m.get('FirstDate')
        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')
        if m.get('SuccessDate') is not None:
            self.success_date = m.get('SuccessDate')
        if m.get('TypeNum') is not None:
            self.type_num = m.get('TypeNum')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetOcIpSoftwareCopyrightResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIpSoftwareCopyrightResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIpSoftwareCopyrightResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIpSoftwareCopyrightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIpSoftwareCopyrightResponseBody = None,
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
            temp_model = GetOcIpSoftwareCopyrightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIpTrademarkRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIpTrademarkResponseBodyData(TeaModel):
    def __init__(
        self,
        agent: str = None,
        apply_date: str = None,
        ent_name: str = None,
        first_pub_date: str = None,
        first_pub_no: str = None,
        image_url: str = None,
        period: str = None,
        reg_num: str = None,
        reg_pub_date: str = None,
        reg_pub_no: str = None,
        trademark_form: str = None,
        trademark_name: str = None,
        trademark_status: str = None,
        trademark_type: str = None,
        type_name: str = None,
    ):
        self.agent = agent
        self.apply_date = apply_date
        self.ent_name = ent_name
        self.first_pub_date = first_pub_date
        self.first_pub_no = first_pub_no
        self.image_url = image_url
        self.period = period
        self.reg_num = reg_num
        self.reg_pub_date = reg_pub_date
        self.reg_pub_no = reg_pub_no
        self.trademark_form = trademark_form
        self.trademark_name = trademark_name
        self.trademark_status = trademark_status
        self.trademark_type = trademark_type
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent is not None:
            result['Agent'] = self.agent
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.first_pub_date is not None:
            result['FirstPubDate'] = self.first_pub_date
        if self.first_pub_no is not None:
            result['FirstPubNo'] = self.first_pub_no
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.period is not None:
            result['Period'] = self.period
        if self.reg_num is not None:
            result['RegNum'] = self.reg_num
        if self.reg_pub_date is not None:
            result['RegPubDate'] = self.reg_pub_date
        if self.reg_pub_no is not None:
            result['RegPubNo'] = self.reg_pub_no
        if self.trademark_form is not None:
            result['TrademarkForm'] = self.trademark_form
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_status is not None:
            result['TrademarkStatus'] = self.trademark_status
        if self.trademark_type is not None:
            result['TrademarkType'] = self.trademark_type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            self.agent = m.get('Agent')
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('FirstPubDate') is not None:
            self.first_pub_date = m.get('FirstPubDate')
        if m.get('FirstPubNo') is not None:
            self.first_pub_no = m.get('FirstPubNo')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegNum') is not None:
            self.reg_num = m.get('RegNum')
        if m.get('RegPubDate') is not None:
            self.reg_pub_date = m.get('RegPubDate')
        if m.get('RegPubNo') is not None:
            self.reg_pub_no = m.get('RegPubNo')
        if m.get('TrademarkForm') is not None:
            self.trademark_form = m.get('TrademarkForm')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkStatus') is not None:
            self.trademark_status = m.get('TrademarkStatus')
        if m.get('TrademarkType') is not None:
            self.trademark_type = m.get('TrademarkType')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class GetOcIpTrademarkResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIpTrademarkResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIpTrademarkResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIpTrademarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIpTrademarkResponseBody = None,
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
            temp_model = GetOcIpTrademarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcIpWorksCopyrightRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcIpWorksCopyrightResponseBodyData(TeaModel):
    def __init__(
        self,
        approval_date: str = None,
        copy_name: str = None,
        copy_num: str = None,
        ent_name: str = None,
        first_date: str = None,
        success_date: str = None,
        type_name: str = None,
    ):
        self.approval_date = approval_date
        self.copy_name = copy_name
        self.copy_num = copy_num
        self.ent_name = ent_name
        self.first_date = first_date
        self.success_date = success_date
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_date is not None:
            result['ApprovalDate'] = self.approval_date
        if self.copy_name is not None:
            result['CopyName'] = self.copy_name
        if self.copy_num is not None:
            result['CopyNum'] = self.copy_num
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.first_date is not None:
            result['FirstDate'] = self.first_date
        if self.success_date is not None:
            result['SuccessDate'] = self.success_date
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalDate') is not None:
            self.approval_date = m.get('ApprovalDate')
        if m.get('CopyName') is not None:
            self.copy_name = m.get('CopyName')
        if m.get('CopyNum') is not None:
            self.copy_num = m.get('CopyNum')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('FirstDate') is not None:
            self.first_date = m.get('FirstDate')
        if m.get('SuccessDate') is not None:
            self.success_date = m.get('SuccessDate')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class GetOcIpWorksCopyrightResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcIpWorksCopyrightResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcIpWorksCopyrightResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcIpWorksCopyrightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcIpWorksCopyrightResponseBody = None,
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
            temp_model = GetOcIpWorksCopyrightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcJusticeAuctionRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcJusticeAuctionResponseBodyData(TeaModel):
    def __init__(
        self,
        auction_date: str = None,
        auction_name: str = None,
        basis: str = None,
        certificate: str = None,
        court: str = None,
        description: str = None,
        document: str = None,
        ent_name: str = None,
        est_price: str = None,
        owner: str = None,
        restrict: str = None,
        start_price: str = None,
    ):
        self.auction_date = auction_date
        self.auction_name = auction_name
        self.basis = basis
        self.certificate = certificate
        self.court = court
        self.description = description
        self.document = document
        self.ent_name = ent_name
        self.est_price = est_price
        self.owner = owner
        self.restrict = restrict
        self.start_price = start_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_date is not None:
            result['AuctionDate'] = self.auction_date
        if self.auction_name is not None:
            result['AuctionName'] = self.auction_name
        if self.basis is not None:
            result['Basis'] = self.basis
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.court is not None:
            result['Court'] = self.court
        if self.description is not None:
            result['Description'] = self.description
        if self.document is not None:
            result['Document'] = self.document
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.est_price is not None:
            result['EstPrice'] = self.est_price
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.restrict is not None:
            result['Restrict'] = self.restrict
        if self.start_price is not None:
            result['StartPrice'] = self.start_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionDate') is not None:
            self.auction_date = m.get('AuctionDate')
        if m.get('AuctionName') is not None:
            self.auction_name = m.get('AuctionName')
        if m.get('Basis') is not None:
            self.basis = m.get('Basis')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Court') is not None:
            self.court = m.get('Court')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Document') is not None:
            self.document = m.get('Document')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('EstPrice') is not None:
            self.est_price = m.get('EstPrice')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Restrict') is not None:
            self.restrict = m.get('Restrict')
        if m.get('StartPrice') is not None:
            self.start_price = m.get('StartPrice')
        return self


class GetOcJusticeAuctionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcJusticeAuctionResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcJusticeAuctionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcJusticeAuctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcJusticeAuctionResponseBody = None,
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
            temp_model = GetOcJusticeAuctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcJusticeCaseFilingRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcJusticeCaseFilingResponseBodyData(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        case_num: str = None,
        case_status: str = None,
        cause_action: str = None,
        end_date: str = None,
        filing_date: str = None,
        hearing_date: str = None,
        judge: str = None,
        party: str = None,
        role: str = None,
    ):
        self.assistant = assistant
        self.case_num = case_num
        self.case_status = case_status
        self.cause_action = cause_action
        self.end_date = end_date
        self.filing_date = filing_date
        self.hearing_date = hearing_date
        self.judge = judge
        self.party = party
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['Assistant'] = self.assistant
        if self.case_num is not None:
            result['CaseNum'] = self.case_num
        if self.case_status is not None:
            result['CaseStatus'] = self.case_status
        if self.cause_action is not None:
            result['CauseAction'] = self.cause_action
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.filing_date is not None:
            result['FilingDate'] = self.filing_date
        if self.hearing_date is not None:
            result['HearingDate'] = self.hearing_date
        if self.judge is not None:
            result['Judge'] = self.judge
        if self.party is not None:
            result['Party'] = self.party
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Assistant') is not None:
            self.assistant = m.get('Assistant')
        if m.get('CaseNum') is not None:
            self.case_num = m.get('CaseNum')
        if m.get('CaseStatus') is not None:
            self.case_status = m.get('CaseStatus')
        if m.get('CauseAction') is not None:
            self.cause_action = m.get('CauseAction')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FilingDate') is not None:
            self.filing_date = m.get('FilingDate')
        if m.get('HearingDate') is not None:
            self.hearing_date = m.get('HearingDate')
        if m.get('Judge') is not None:
            self.judge = m.get('Judge')
        if m.get('Party') is not None:
            self.party = m.get('Party')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class GetOcJusticeCaseFilingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcJusticeCaseFilingResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcJusticeCaseFilingResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcJusticeCaseFilingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcJusticeCaseFilingResponseBody = None,
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
            temp_model = GetOcJusticeCaseFilingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcJusticeCourtAnnouncementRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcJusticeCourtAnnouncementResponseBodyData(TeaModel):
    def __init__(
        self,
        case_num: str = None,
        cause_action: str = None,
        court: str = None,
        department: str = None,
        hearing_date: str = None,
        judge: str = None,
        party: str = None,
        title: str = None,
        tribunal: str = None,
    ):
        self.case_num = case_num
        self.cause_action = cause_action
        self.court = court
        self.department = department
        self.hearing_date = hearing_date
        self.judge = judge
        self.party = party
        self.title = title
        self.tribunal = tribunal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_num is not None:
            result['CaseNum'] = self.case_num
        if self.cause_action is not None:
            result['CauseAction'] = self.cause_action
        if self.court is not None:
            result['Court'] = self.court
        if self.department is not None:
            result['Department'] = self.department
        if self.hearing_date is not None:
            result['HearingDate'] = self.hearing_date
        if self.judge is not None:
            result['Judge'] = self.judge
        if self.party is not None:
            result['Party'] = self.party
        if self.title is not None:
            result['Title'] = self.title
        if self.tribunal is not None:
            result['Tribunal'] = self.tribunal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseNum') is not None:
            self.case_num = m.get('CaseNum')
        if m.get('CauseAction') is not None:
            self.cause_action = m.get('CauseAction')
        if m.get('Court') is not None:
            self.court = m.get('Court')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('HearingDate') is not None:
            self.hearing_date = m.get('HearingDate')
        if m.get('Judge') is not None:
            self.judge = m.get('Judge')
        if m.get('Party') is not None:
            self.party = m.get('Party')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Tribunal') is not None:
            self.tribunal = m.get('Tribunal')
        return self


class GetOcJusticeCourtAnnouncementResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcJusticeCourtAnnouncementResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcJusticeCourtAnnouncementResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcJusticeCourtAnnouncementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcJusticeCourtAnnouncementResponseBody = None,
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
            temp_model = GetOcJusticeCourtAnnouncementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcJusticeCourtNoticeRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcJusticeCourtNoticeResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        court: str = None,
        party: str = None,
        public_date: str = None,
        type: str = None,
    ):
        self.content = content
        self.court = court
        self.party = party
        self.public_date = public_date
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
        if self.court is not None:
            result['Court'] = self.court
        if self.party is not None:
            result['Party'] = self.party
        if self.public_date is not None:
            result['PublicDate'] = self.public_date
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Court') is not None:
            self.court = m.get('Court')
        if m.get('Party') is not None:
            self.party = m.get('Party')
        if m.get('PublicDate') is not None:
            self.public_date = m.get('PublicDate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetOcJusticeCourtNoticeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcJusticeCourtNoticeResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcJusticeCourtNoticeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcJusticeCourtNoticeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcJusticeCourtNoticeResponseBody = None,
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
            temp_model = GetOcJusticeCourtNoticeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcJusticeDishonestyRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcJusticeDishonestyResponseBodyData(TeaModel):
    def __init__(
        self,
        amount: str = None,
        case_num: str = None,
        court: str = None,
        ent_name: str = None,
        execute_department: str = None,
        execution_desc: str = None,
        execution_status: str = None,
        filing_date: str = None,
        final_duty: str = None,
        from_case_num: str = None,
        legal_name: str = None,
        province: str = None,
        publish_date: str = None,
        social_credit_code: str = None,
    ):
        self.amount = amount
        self.case_num = case_num
        self.court = court
        self.ent_name = ent_name
        self.execute_department = execute_department
        self.execution_desc = execution_desc
        self.execution_status = execution_status
        self.filing_date = filing_date
        self.final_duty = final_duty
        self.from_case_num = from_case_num
        self.legal_name = legal_name
        self.province = province
        self.publish_date = publish_date
        self.social_credit_code = social_credit_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.case_num is not None:
            result['CaseNum'] = self.case_num
        if self.court is not None:
            result['Court'] = self.court
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.execute_department is not None:
            result['ExecuteDepartment'] = self.execute_department
        if self.execution_desc is not None:
            result['ExecutionDesc'] = self.execution_desc
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.filing_date is not None:
            result['FilingDate'] = self.filing_date
        if self.final_duty is not None:
            result['FinalDuty'] = self.final_duty
        if self.from_case_num is not None:
            result['FromCaseNum'] = self.from_case_num
        if self.legal_name is not None:
            result['LegalName'] = self.legal_name
        if self.province is not None:
            result['Province'] = self.province
        if self.publish_date is not None:
            result['PublishDate'] = self.publish_date
        if self.social_credit_code is not None:
            result['SocialCreditCode'] = self.social_credit_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('CaseNum') is not None:
            self.case_num = m.get('CaseNum')
        if m.get('Court') is not None:
            self.court = m.get('Court')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('ExecuteDepartment') is not None:
            self.execute_department = m.get('ExecuteDepartment')
        if m.get('ExecutionDesc') is not None:
            self.execution_desc = m.get('ExecutionDesc')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('FilingDate') is not None:
            self.filing_date = m.get('FilingDate')
        if m.get('FinalDuty') is not None:
            self.final_duty = m.get('FinalDuty')
        if m.get('FromCaseNum') is not None:
            self.from_case_num = m.get('FromCaseNum')
        if m.get('LegalName') is not None:
            self.legal_name = m.get('LegalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('PublishDate') is not None:
            self.publish_date = m.get('PublishDate')
        if m.get('SocialCreditCode') is not None:
            self.social_credit_code = m.get('SocialCreditCode')
        return self


class GetOcJusticeDishonestyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcJusticeDishonestyResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcJusticeDishonestyResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcJusticeDishonestyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcJusticeDishonestyResponseBody = None,
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
            temp_model = GetOcJusticeDishonestyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcJusticeExecutedRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcJusticeExecutedResponseBodyData(TeaModel):
    def __init__(
        self,
        amount: str = None,
        case_num: str = None,
        court: str = None,
        filing_date: str = None,
    ):
        self.amount = amount
        self.case_num = case_num
        self.court = court
        self.filing_date = filing_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.case_num is not None:
            result['CaseNum'] = self.case_num
        if self.court is not None:
            result['Court'] = self.court
        if self.filing_date is not None:
            result['FilingDate'] = self.filing_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('CaseNum') is not None:
            self.case_num = m.get('CaseNum')
        if m.get('Court') is not None:
            self.court = m.get('Court')
        if m.get('FilingDate') is not None:
            self.filing_date = m.get('FilingDate')
        return self


class GetOcJusticeExecutedResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcJusticeExecutedResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcJusticeExecutedResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcJusticeExecutedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcJusticeExecutedResponseBody = None,
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
            temp_model = GetOcJusticeExecutedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcJusticeJudgementDocRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcJusticeJudgementDocResponseBodyData(TeaModel):
    def __init__(
        self,
        case_flow: str = None,
        case_num: str = None,
        case_type: str = None,
        cause_action: str = None,
        court: str = None,
        defendant: str = None,
        judge_date: str = None,
        judge_result: str = None,
        judge_type: str = None,
        party: str = None,
        plaintiff: str = None,
        public_date: str = None,
        role: str = None,
        sub_amount: str = None,
        title: str = None,
    ):
        self.case_flow = case_flow
        self.case_num = case_num
        self.case_type = case_type
        self.cause_action = cause_action
        self.court = court
        self.defendant = defendant
        self.judge_date = judge_date
        self.judge_result = judge_result
        self.judge_type = judge_type
        self.party = party
        self.plaintiff = plaintiff
        self.public_date = public_date
        self.role = role
        self.sub_amount = sub_amount
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_flow is not None:
            result['CaseFlow'] = self.case_flow
        if self.case_num is not None:
            result['CaseNum'] = self.case_num
        if self.case_type is not None:
            result['CaseType'] = self.case_type
        if self.cause_action is not None:
            result['CauseAction'] = self.cause_action
        if self.court is not None:
            result['Court'] = self.court
        if self.defendant is not None:
            result['Defendant'] = self.defendant
        if self.judge_date is not None:
            result['JudgeDate'] = self.judge_date
        if self.judge_result is not None:
            result['JudgeResult'] = self.judge_result
        if self.judge_type is not None:
            result['JudgeType'] = self.judge_type
        if self.party is not None:
            result['Party'] = self.party
        if self.plaintiff is not None:
            result['Plaintiff'] = self.plaintiff
        if self.public_date is not None:
            result['PublicDate'] = self.public_date
        if self.role is not None:
            result['Role'] = self.role
        if self.sub_amount is not None:
            result['SubAmount'] = self.sub_amount
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseFlow') is not None:
            self.case_flow = m.get('CaseFlow')
        if m.get('CaseNum') is not None:
            self.case_num = m.get('CaseNum')
        if m.get('CaseType') is not None:
            self.case_type = m.get('CaseType')
        if m.get('CauseAction') is not None:
            self.cause_action = m.get('CauseAction')
        if m.get('Court') is not None:
            self.court = m.get('Court')
        if m.get('Defendant') is not None:
            self.defendant = m.get('Defendant')
        if m.get('JudgeDate') is not None:
            self.judge_date = m.get('JudgeDate')
        if m.get('JudgeResult') is not None:
            self.judge_result = m.get('JudgeResult')
        if m.get('JudgeType') is not None:
            self.judge_type = m.get('JudgeType')
        if m.get('Party') is not None:
            self.party = m.get('Party')
        if m.get('Plaintiff') is not None:
            self.plaintiff = m.get('Plaintiff')
        if m.get('PublicDate') is not None:
            self.public_date = m.get('PublicDate')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SubAmount') is not None:
            self.sub_amount = m.get('SubAmount')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetOcJusticeJudgementDocResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcJusticeJudgementDocResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcJusticeJudgementDocResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcJusticeJudgementDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcJusticeJudgementDocResponseBody = None,
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
            temp_model = GetOcJusticeJudgementDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcJusticeLimitHighConsumeRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcJusticeLimitHighConsumeResponseBodyData(TeaModel):
    def __init__(
        self,
        case_num: str = None,
        cause_action: str = None,
        company_name: str = None,
        court: str = None,
        execution_applicant: str = None,
        filing_date: str = None,
        name: str = None,
        publish_date: str = None,
    ):
        self.case_num = case_num
        self.cause_action = cause_action
        self.company_name = company_name
        self.court = court
        self.execution_applicant = execution_applicant
        self.filing_date = filing_date
        self.name = name
        self.publish_date = publish_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_num is not None:
            result['CaseNum'] = self.case_num
        if self.cause_action is not None:
            result['CauseAction'] = self.cause_action
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.court is not None:
            result['Court'] = self.court
        if self.execution_applicant is not None:
            result['ExecutionApplicant'] = self.execution_applicant
        if self.filing_date is not None:
            result['FilingDate'] = self.filing_date
        if self.name is not None:
            result['Name'] = self.name
        if self.publish_date is not None:
            result['PublishDate'] = self.publish_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseNum') is not None:
            self.case_num = m.get('CaseNum')
        if m.get('CauseAction') is not None:
            self.cause_action = m.get('CauseAction')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('Court') is not None:
            self.court = m.get('Court')
        if m.get('ExecutionApplicant') is not None:
            self.execution_applicant = m.get('ExecutionApplicant')
        if m.get('FilingDate') is not None:
            self.filing_date = m.get('FilingDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PublishDate') is not None:
            self.publish_date = m.get('PublishDate')
        return self


class GetOcJusticeLimitHighConsumeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcJusticeLimitHighConsumeResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcJusticeLimitHighConsumeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcJusticeLimitHighConsumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcJusticeLimitHighConsumeResponseBody = None,
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
            temp_model = GetOcJusticeLimitHighConsumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcJusticeTerminalCaseRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcJusticeTerminalCaseResponseBodyData(TeaModel):
    def __init__(
        self,
        case_num: str = None,
        court: str = None,
        ent_name: str = None,
        exec_amount: str = None,
        fail_perform_amount: str = None,
        filing_date: str = None,
        name: str = None,
        terminal_num: str = None,
        terminate_date: str = None,
    ):
        self.case_num = case_num
        self.court = court
        self.ent_name = ent_name
        self.exec_amount = exec_amount
        self.fail_perform_amount = fail_perform_amount
        self.filing_date = filing_date
        self.name = name
        self.terminal_num = terminal_num
        self.terminate_date = terminate_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_num is not None:
            result['CaseNum'] = self.case_num
        if self.court is not None:
            result['Court'] = self.court
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.exec_amount is not None:
            result['ExecAmount'] = self.exec_amount
        if self.fail_perform_amount is not None:
            result['FailPerformAmount'] = self.fail_perform_amount
        if self.filing_date is not None:
            result['FilingDate'] = self.filing_date
        if self.name is not None:
            result['Name'] = self.name
        if self.terminal_num is not None:
            result['TerminalNum'] = self.terminal_num
        if self.terminate_date is not None:
            result['TerminateDate'] = self.terminate_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseNum') is not None:
            self.case_num = m.get('CaseNum')
        if m.get('Court') is not None:
            self.court = m.get('Court')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('ExecAmount') is not None:
            self.exec_amount = m.get('ExecAmount')
        if m.get('FailPerformAmount') is not None:
            self.fail_perform_amount = m.get('FailPerformAmount')
        if m.get('FilingDate') is not None:
            self.filing_date = m.get('FilingDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TerminalNum') is not None:
            self.terminal_num = m.get('TerminalNum')
        if m.get('TerminateDate') is not None:
            self.terminate_date = m.get('TerminateDate')
        return self


class GetOcJusticeTerminalCaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcJusticeTerminalCaseResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcJusticeTerminalCaseResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcJusticeTerminalCaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcJusticeTerminalCaseResponseBody = None,
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
            temp_model = GetOcJusticeTerminalCaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcListedCompanyRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcListedCompanyResponseBodyData(TeaModel):
    def __init__(
        self,
        circulation_market_value: str = None,
        ent_name: str = None,
        ent_name_eng: str = None,
        list_date: str = None,
        securities_code: str = None,
        securities_market: str = None,
        securities_name: str = None,
        total_flow_shares: str = None,
        total_shares: str = None,
    ):
        self.circulation_market_value = circulation_market_value
        self.ent_name = ent_name
        self.ent_name_eng = ent_name_eng
        self.list_date = list_date
        self.securities_code = securities_code
        self.securities_market = securities_market
        self.securities_name = securities_name
        self.total_flow_shares = total_flow_shares
        self.total_shares = total_shares

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.circulation_market_value is not None:
            result['CirculationMarketValue'] = self.circulation_market_value
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.ent_name_eng is not None:
            result['EntNameEng'] = self.ent_name_eng
        if self.list_date is not None:
            result['ListDate'] = self.list_date
        if self.securities_code is not None:
            result['SecuritiesCode'] = self.securities_code
        if self.securities_market is not None:
            result['SecuritiesMarket'] = self.securities_market
        if self.securities_name is not None:
            result['SecuritiesName'] = self.securities_name
        if self.total_flow_shares is not None:
            result['TotalFlowShares'] = self.total_flow_shares
        if self.total_shares is not None:
            result['TotalShares'] = self.total_shares
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CirculationMarketValue') is not None:
            self.circulation_market_value = m.get('CirculationMarketValue')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('EntNameEng') is not None:
            self.ent_name_eng = m.get('EntNameEng')
        if m.get('ListDate') is not None:
            self.list_date = m.get('ListDate')
        if m.get('SecuritiesCode') is not None:
            self.securities_code = m.get('SecuritiesCode')
        if m.get('SecuritiesMarket') is not None:
            self.securities_market = m.get('SecuritiesMarket')
        if m.get('SecuritiesName') is not None:
            self.securities_name = m.get('SecuritiesName')
        if m.get('TotalFlowShares') is not None:
            self.total_flow_shares = m.get('TotalFlowShares')
        if m.get('TotalShares') is not None:
            self.total_shares = m.get('TotalShares')
        return self


class GetOcListedCompanyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcListedCompanyResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcListedCompanyResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcListedCompanyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcListedCompanyResponseBody = None,
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
            temp_model = GetOcListedCompanyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcNegativeAdminPunishmentRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcNegativeAdminPunishmentResponseBodyData(TeaModel):
    def __init__(
        self,
        department: str = None,
        ent_name: str = None,
        illegal_type: str = None,
        law_basis: str = None,
        public_date: str = None,
        punish_date: str = None,
        punish_num: str = None,
        punish_result: str = None,
    ):
        self.department = department
        self.ent_name = ent_name
        self.illegal_type = illegal_type
        self.law_basis = law_basis
        self.public_date = public_date
        self.punish_date = punish_date
        self.punish_num = punish_num
        self.punish_result = punish_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department is not None:
            result['Department'] = self.department
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.illegal_type is not None:
            result['IllegalType'] = self.illegal_type
        if self.law_basis is not None:
            result['LawBasis'] = self.law_basis
        if self.public_date is not None:
            result['PublicDate'] = self.public_date
        if self.punish_date is not None:
            result['PunishDate'] = self.punish_date
        if self.punish_num is not None:
            result['PunishNum'] = self.punish_num
        if self.punish_result is not None:
            result['PunishResult'] = self.punish_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('IllegalType') is not None:
            self.illegal_type = m.get('IllegalType')
        if m.get('LawBasis') is not None:
            self.law_basis = m.get('LawBasis')
        if m.get('PublicDate') is not None:
            self.public_date = m.get('PublicDate')
        if m.get('PunishDate') is not None:
            self.punish_date = m.get('PunishDate')
        if m.get('PunishNum') is not None:
            self.punish_num = m.get('PunishNum')
        if m.get('PunishResult') is not None:
            self.punish_result = m.get('PunishResult')
        return self


class GetOcNegativeAdminPunishmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcNegativeAdminPunishmentResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcNegativeAdminPunishmentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcNegativeAdminPunishmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcNegativeAdminPunishmentResponseBody = None,
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
            temp_model = GetOcNegativeAdminPunishmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcNegativeCustomsPunishmentRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcNegativeCustomsPunishmentResponseBodyData(TeaModel):
    def __init__(
        self,
        basis: str = None,
        case_no: str = None,
        customs: str = None,
        customs_no: str = None,
        legal_name: str = None,
        punish_date: str = None,
        punish_type: str = None,
        title: str = None,
    ):
        self.basis = basis
        self.case_no = case_no
        self.customs = customs
        self.customs_no = customs_no
        self.legal_name = legal_name
        self.punish_date = punish_date
        self.punish_type = punish_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basis is not None:
            result['Basis'] = self.basis
        if self.case_no is not None:
            result['CaseNo'] = self.case_no
        if self.customs is not None:
            result['Customs'] = self.customs
        if self.customs_no is not None:
            result['CustomsNo'] = self.customs_no
        if self.legal_name is not None:
            result['LegalName'] = self.legal_name
        if self.punish_date is not None:
            result['PunishDate'] = self.punish_date
        if self.punish_type is not None:
            result['PunishType'] = self.punish_type
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Basis') is not None:
            self.basis = m.get('Basis')
        if m.get('CaseNo') is not None:
            self.case_no = m.get('CaseNo')
        if m.get('Customs') is not None:
            self.customs = m.get('Customs')
        if m.get('CustomsNo') is not None:
            self.customs_no = m.get('CustomsNo')
        if m.get('LegalName') is not None:
            self.legal_name = m.get('LegalName')
        if m.get('PunishDate') is not None:
            self.punish_date = m.get('PunishDate')
        if m.get('PunishType') is not None:
            self.punish_type = m.get('PunishType')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetOcNegativeCustomsPunishmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcNegativeCustomsPunishmentResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcNegativeCustomsPunishmentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcNegativeCustomsPunishmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcNegativeCustomsPunishmentResponseBody = None,
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
            temp_model = GetOcNegativeCustomsPunishmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcNegativeEnvironmentPunishmentRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcNegativeEnvironmentPunishmentResponseBodyData(TeaModel):
    def __init__(
        self,
        department: str = None,
        ent_name: str = None,
        exec_status: str = None,
        punish_basis: str = None,
        punish_content: str = None,
        punish_date: str = None,
        punish_law: str = None,
        punish_num: str = None,
        punish_res: str = None,
    ):
        self.department = department
        self.ent_name = ent_name
        self.exec_status = exec_status
        self.punish_basis = punish_basis
        self.punish_content = punish_content
        self.punish_date = punish_date
        self.punish_law = punish_law
        self.punish_num = punish_num
        self.punish_res = punish_res

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department is not None:
            result['Department'] = self.department
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.exec_status is not None:
            result['ExecStatus'] = self.exec_status
        if self.punish_basis is not None:
            result['PunishBasis'] = self.punish_basis
        if self.punish_content is not None:
            result['PunishContent'] = self.punish_content
        if self.punish_date is not None:
            result['PunishDate'] = self.punish_date
        if self.punish_law is not None:
            result['PunishLaw'] = self.punish_law
        if self.punish_num is not None:
            result['PunishNum'] = self.punish_num
        if self.punish_res is not None:
            result['PunishRes'] = self.punish_res
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('ExecStatus') is not None:
            self.exec_status = m.get('ExecStatus')
        if m.get('PunishBasis') is not None:
            self.punish_basis = m.get('PunishBasis')
        if m.get('PunishContent') is not None:
            self.punish_content = m.get('PunishContent')
        if m.get('PunishDate') is not None:
            self.punish_date = m.get('PunishDate')
        if m.get('PunishLaw') is not None:
            self.punish_law = m.get('PunishLaw')
        if m.get('PunishNum') is not None:
            self.punish_num = m.get('PunishNum')
        if m.get('PunishRes') is not None:
            self.punish_res = m.get('PunishRes')
        return self


class GetOcNegativeEnvironmentPunishmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcNegativeEnvironmentPunishmentResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcNegativeEnvironmentPunishmentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcNegativeEnvironmentPunishmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcNegativeEnvironmentPunishmentResponseBody = None,
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
            temp_model = GetOcNegativeEnvironmentPunishmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcNegativeFoodDrugPunishmentRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcNegativeFoodDrugPunishmentResponseBodyData(TeaModel):
    def __init__(
        self,
        department: str = None,
        ent_name: str = None,
        illegal_type: str = None,
        law_basis: str = None,
        public_date: str = None,
        punish_date: str = None,
        punish_num: str = None,
        punish_result: str = None,
    ):
        self.department = department
        self.ent_name = ent_name
        self.illegal_type = illegal_type
        self.law_basis = law_basis
        self.public_date = public_date
        self.punish_date = punish_date
        self.punish_num = punish_num
        self.punish_result = punish_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department is not None:
            result['Department'] = self.department
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.illegal_type is not None:
            result['IllegalType'] = self.illegal_type
        if self.law_basis is not None:
            result['LawBasis'] = self.law_basis
        if self.public_date is not None:
            result['PublicDate'] = self.public_date
        if self.punish_date is not None:
            result['PunishDate'] = self.punish_date
        if self.punish_num is not None:
            result['PunishNum'] = self.punish_num
        if self.punish_result is not None:
            result['PunishResult'] = self.punish_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('IllegalType') is not None:
            self.illegal_type = m.get('IllegalType')
        if m.get('LawBasis') is not None:
            self.law_basis = m.get('LawBasis')
        if m.get('PublicDate') is not None:
            self.public_date = m.get('PublicDate')
        if m.get('PunishDate') is not None:
            self.punish_date = m.get('PunishDate')
        if m.get('PunishNum') is not None:
            self.punish_num = m.get('PunishNum')
        if m.get('PunishResult') is not None:
            self.punish_result = m.get('PunishResult')
        return self


class GetOcNegativeFoodDrugPunishmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcNegativeFoodDrugPunishmentResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcNegativeFoodDrugPunishmentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcNegativeFoodDrugPunishmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcNegativeFoodDrugPunishmentResponseBody = None,
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
            temp_model = GetOcNegativeFoodDrugPunishmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcNegativeQualityPunishmentRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcNegativeQualityPunishmentResponseBodyData(TeaModel):
    def __init__(
        self,
        department: str = None,
        ent_name: str = None,
        event_date: str = None,
        event_result: str = None,
        pub_date: str = None,
        title: str = None,
    ):
        self.department = department
        self.ent_name = ent_name
        self.event_date = event_date
        self.event_result = event_result
        self.pub_date = pub_date
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department is not None:
            result['Department'] = self.department
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.event_date is not None:
            result['EventDate'] = self.event_date
        if self.event_result is not None:
            result['EventResult'] = self.event_result
        if self.pub_date is not None:
            result['PubDate'] = self.pub_date
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('EventDate') is not None:
            self.event_date = m.get('EventDate')
        if m.get('EventResult') is not None:
            self.event_result = m.get('EventResult')
        if m.get('PubDate') is not None:
            self.pub_date = m.get('PubDate')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetOcNegativeQualityPunishmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcNegativeQualityPunishmentResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcNegativeQualityPunishmentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcNegativeQualityPunishmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcNegativeQualityPunishmentResponseBody = None,
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
            temp_model = GetOcNegativeQualityPunishmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcOperationBiddingRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcOperationBiddingResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_ent_name: str = None,
        bid_industry: str = None,
        bid_title: str = None,
        bid_type: str = None,
        content: str = None,
        ent_name: str = None,
        info_type: str = None,
        opening_time: str = None,
        project_amount: str = None,
        project_name: str = None,
        project_num: str = None,
        public_date: str = None,
        region_name: str = None,
        sub_type: str = None,
        tender_ent_name: str = None,
        winner_ent_name: str = None,
    ):
        self.agent_ent_name = agent_ent_name
        self.bid_industry = bid_industry
        self.bid_title = bid_title
        self.bid_type = bid_type
        self.content = content
        self.ent_name = ent_name
        self.info_type = info_type
        self.opening_time = opening_time
        self.project_amount = project_amount
        self.project_name = project_name
        self.project_num = project_num
        self.public_date = public_date
        self.region_name = region_name
        self.sub_type = sub_type
        self.tender_ent_name = tender_ent_name
        self.winner_ent_name = winner_ent_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_ent_name is not None:
            result['AgentEntName'] = self.agent_ent_name
        if self.bid_industry is not None:
            result['BidIndustry'] = self.bid_industry
        if self.bid_title is not None:
            result['BidTitle'] = self.bid_title
        if self.bid_type is not None:
            result['BidType'] = self.bid_type
        if self.content is not None:
            result['Content'] = self.content
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.info_type is not None:
            result['InfoType'] = self.info_type
        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time
        if self.project_amount is not None:
            result['ProjectAmount'] = self.project_amount
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_num is not None:
            result['ProjectNum'] = self.project_num
        if self.public_date is not None:
            result['PublicDate'] = self.public_date
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.tender_ent_name is not None:
            result['TenderEntName'] = self.tender_ent_name
        if self.winner_ent_name is not None:
            result['WinnerEntName'] = self.winner_ent_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentEntName') is not None:
            self.agent_ent_name = m.get('AgentEntName')
        if m.get('BidIndustry') is not None:
            self.bid_industry = m.get('BidIndustry')
        if m.get('BidTitle') is not None:
            self.bid_title = m.get('BidTitle')
        if m.get('BidType') is not None:
            self.bid_type = m.get('BidType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')
        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')
        if m.get('ProjectAmount') is not None:
            self.project_amount = m.get('ProjectAmount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectNum') is not None:
            self.project_num = m.get('ProjectNum')
        if m.get('PublicDate') is not None:
            self.public_date = m.get('PublicDate')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('TenderEntName') is not None:
            self.tender_ent_name = m.get('TenderEntName')
        if m.get('WinnerEntName') is not None:
            self.winner_ent_name = m.get('WinnerEntName')
        return self


class GetOcOperationBiddingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcOperationBiddingResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcOperationBiddingResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcOperationBiddingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcOperationBiddingResponseBody = None,
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
            temp_model = GetOcOperationBiddingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcOperationCustomsRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcOperationCustomsResponseBodyData(TeaModel):
    def __init__(
        self,
        admin_region_name: str = None,
        annual_report: str = None,
        business_cate: str = None,
        cancel_flag: str = None,
        credit_levels_new: str = None,
        customs_num: str = None,
        customs_reg: str = None,
        eco_region_name: str = None,
        elect_type: str = None,
        ent_name: str = None,
        ident_code: str = None,
        ident_date: str = None,
        industry_type: str = None,
        reg_date: str = None,
        special_area: str = None,
        valid_date: str = None,
    ):
        self.admin_region_name = admin_region_name
        self.annual_report = annual_report
        self.business_cate = business_cate
        self.cancel_flag = cancel_flag
        self.credit_levels_new = credit_levels_new
        self.customs_num = customs_num
        self.customs_reg = customs_reg
        self.eco_region_name = eco_region_name
        self.elect_type = elect_type
        self.ent_name = ent_name
        self.ident_code = ident_code
        self.ident_date = ident_date
        self.industry_type = industry_type
        self.reg_date = reg_date
        self.special_area = special_area
        self.valid_date = valid_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_region_name is not None:
            result['AdminRegionName'] = self.admin_region_name
        if self.annual_report is not None:
            result['AnnualReport'] = self.annual_report
        if self.business_cate is not None:
            result['BusinessCate'] = self.business_cate
        if self.cancel_flag is not None:
            result['CancelFlag'] = self.cancel_flag
        if self.credit_levels_new is not None:
            result['CreditLevelsNew'] = self.credit_levels_new
        if self.customs_num is not None:
            result['CustomsNum'] = self.customs_num
        if self.customs_reg is not None:
            result['CustomsReg'] = self.customs_reg
        if self.eco_region_name is not None:
            result['EcoRegionName'] = self.eco_region_name
        if self.elect_type is not None:
            result['ElectType'] = self.elect_type
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.ident_code is not None:
            result['IdentCode'] = self.ident_code
        if self.ident_date is not None:
            result['IdentDate'] = self.ident_date
        if self.industry_type is not None:
            result['IndustryType'] = self.industry_type
        if self.reg_date is not None:
            result['RegDate'] = self.reg_date
        if self.special_area is not None:
            result['SpecialArea'] = self.special_area
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminRegionName') is not None:
            self.admin_region_name = m.get('AdminRegionName')
        if m.get('AnnualReport') is not None:
            self.annual_report = m.get('AnnualReport')
        if m.get('BusinessCate') is not None:
            self.business_cate = m.get('BusinessCate')
        if m.get('CancelFlag') is not None:
            self.cancel_flag = m.get('CancelFlag')
        if m.get('CreditLevelsNew') is not None:
            self.credit_levels_new = m.get('CreditLevelsNew')
        if m.get('CustomsNum') is not None:
            self.customs_num = m.get('CustomsNum')
        if m.get('CustomsReg') is not None:
            self.customs_reg = m.get('CustomsReg')
        if m.get('EcoRegionName') is not None:
            self.eco_region_name = m.get('EcoRegionName')
        if m.get('ElectType') is not None:
            self.elect_type = m.get('ElectType')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('IdentCode') is not None:
            self.ident_code = m.get('IdentCode')
        if m.get('IdentDate') is not None:
            self.ident_date = m.get('IdentDate')
        if m.get('IndustryType') is not None:
            self.industry_type = m.get('IndustryType')
        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')
        if m.get('SpecialArea') is not None:
            self.special_area = m.get('SpecialArea')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        return self


class GetOcOperationCustomsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcOperationCustomsResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcOperationCustomsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcOperationCustomsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcOperationCustomsResponseBody = None,
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
            temp_model = GetOcOperationCustomsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcOperationPurchaseLandRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcOperationPurchaseLandResponseBodyData(TeaModel):
    def __init__(
        self,
        area: str = None,
        department: str = None,
        electronic_no: str = None,
        ent_name: str = None,
        industry: str = None,
        land_level: str = None,
        land_source: str = None,
        land_use: str = None,
        location: str = None,
        price: str = None,
        project_name: str = None,
        promise_delivery_date: str = None,
        promise_end_date: str = None,
        promise_start_date: str = None,
        region_name: str = None,
        release_date: str = None,
        signing_mode: str = None,
        use_year: str = None,
        volume_fraction_lower_bound: str = None,
        volume_fraction_upper_bound: str = None,
    ):
        self.area = area
        self.department = department
        self.electronic_no = electronic_no
        self.ent_name = ent_name
        self.industry = industry
        self.land_level = land_level
        self.land_source = land_source
        self.land_use = land_use
        self.location = location
        self.price = price
        self.project_name = project_name
        self.promise_delivery_date = promise_delivery_date
        self.promise_end_date = promise_end_date
        self.promise_start_date = promise_start_date
        self.region_name = region_name
        self.release_date = release_date
        self.signing_mode = signing_mode
        self.use_year = use_year
        self.volume_fraction_lower_bound = volume_fraction_lower_bound
        self.volume_fraction_upper_bound = volume_fraction_upper_bound

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.department is not None:
            result['Department'] = self.department
        if self.electronic_no is not None:
            result['ElectronicNo'] = self.electronic_no
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.land_level is not None:
            result['LandLevel'] = self.land_level
        if self.land_source is not None:
            result['LandSource'] = self.land_source
        if self.land_use is not None:
            result['LandUse'] = self.land_use
        if self.location is not None:
            result['Location'] = self.location
        if self.price is not None:
            result['Price'] = self.price
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.promise_delivery_date is not None:
            result['PromiseDeliveryDate'] = self.promise_delivery_date
        if self.promise_end_date is not None:
            result['PromiseEndDate'] = self.promise_end_date
        if self.promise_start_date is not None:
            result['PromiseStartDate'] = self.promise_start_date
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.release_date is not None:
            result['ReleaseDate'] = self.release_date
        if self.signing_mode is not None:
            result['SigningMode'] = self.signing_mode
        if self.use_year is not None:
            result['UseYear'] = self.use_year
        if self.volume_fraction_lower_bound is not None:
            result['VolumeFractionLowerBound'] = self.volume_fraction_lower_bound
        if self.volume_fraction_upper_bound is not None:
            result['VolumeFractionUpperBound'] = self.volume_fraction_upper_bound
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('ElectronicNo') is not None:
            self.electronic_no = m.get('ElectronicNo')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('LandLevel') is not None:
            self.land_level = m.get('LandLevel')
        if m.get('LandSource') is not None:
            self.land_source = m.get('LandSource')
        if m.get('LandUse') is not None:
            self.land_use = m.get('LandUse')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('PromiseDeliveryDate') is not None:
            self.promise_delivery_date = m.get('PromiseDeliveryDate')
        if m.get('PromiseEndDate') is not None:
            self.promise_end_date = m.get('PromiseEndDate')
        if m.get('PromiseStartDate') is not None:
            self.promise_start_date = m.get('PromiseStartDate')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('ReleaseDate') is not None:
            self.release_date = m.get('ReleaseDate')
        if m.get('SigningMode') is not None:
            self.signing_mode = m.get('SigningMode')
        if m.get('UseYear') is not None:
            self.use_year = m.get('UseYear')
        if m.get('VolumeFractionLowerBound') is not None:
            self.volume_fraction_lower_bound = m.get('VolumeFractionLowerBound')
        if m.get('VolumeFractionUpperBound') is not None:
            self.volume_fraction_upper_bound = m.get('VolumeFractionUpperBound')
        return self


class GetOcOperationPurchaseLandResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcOperationPurchaseLandResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcOperationPurchaseLandResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcOperationPurchaseLandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcOperationPurchaseLandResponseBody = None,
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
            temp_model = GetOcOperationPurchaseLandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcOperationRecruitmentRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcOperationRecruitmentResponseBodyData(TeaModel):
    def __init__(
        self,
        benefit_list: str = None,
        description: str = None,
        education: str = None,
        end_date: str = None,
        ent_name: str = None,
        experience: str = None,
        page_url: str = None,
        publish_date: str = None,
        recruiting_address: str = None,
        recruiting_name: str = None,
        salary: str = None,
        start_date: str = None,
    ):
        self.benefit_list = benefit_list
        self.description = description
        self.education = education
        self.end_date = end_date
        self.ent_name = ent_name
        self.experience = experience
        self.page_url = page_url
        self.publish_date = publish_date
        self.recruiting_address = recruiting_address
        self.recruiting_name = recruiting_name
        self.salary = salary
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.benefit_list is not None:
            result['BenefitList'] = self.benefit_list
        if self.description is not None:
            result['Description'] = self.description
        if self.education is not None:
            result['Education'] = self.education
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.experience is not None:
            result['Experience'] = self.experience
        if self.page_url is not None:
            result['PageUrl'] = self.page_url
        if self.publish_date is not None:
            result['PublishDate'] = self.publish_date
        if self.recruiting_address is not None:
            result['RecruitingAddress'] = self.recruiting_address
        if self.recruiting_name is not None:
            result['RecruitingName'] = self.recruiting_name
        if self.salary is not None:
            result['Salary'] = self.salary
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BenefitList') is not None:
            self.benefit_list = m.get('BenefitList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Education') is not None:
            self.education = m.get('Education')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('Experience') is not None:
            self.experience = m.get('Experience')
        if m.get('PageUrl') is not None:
            self.page_url = m.get('PageUrl')
        if m.get('PublishDate') is not None:
            self.publish_date = m.get('PublishDate')
        if m.get('RecruitingAddress') is not None:
            self.recruiting_address = m.get('RecruitingAddress')
        if m.get('RecruitingName') is not None:
            self.recruiting_name = m.get('RecruitingName')
        if m.get('Salary') is not None:
            self.salary = m.get('Salary')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetOcOperationRecruitmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcOperationRecruitmentResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcOperationRecruitmentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcOperationRecruitmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcOperationRecruitmentResponseBody = None,
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
            temp_model = GetOcOperationRecruitmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcProductBandRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcProductBandResponseBodyData(TeaModel):
    def __init__(
        self,
        brand_introduction: str = None,
        device: str = None,
        ent_name: str = None,
        product_introduction: str = None,
        product_logo: str = None,
        product_name: str = None,
        product_tag: str = None,
        product_website: str = None,
    ):
        self.brand_introduction = brand_introduction
        self.device = device
        self.ent_name = ent_name
        self.product_introduction = product_introduction
        self.product_logo = product_logo
        self.product_name = product_name
        self.product_tag = product_tag
        self.product_website = product_website

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.brand_introduction is not None:
            result['BrandIntroduction'] = self.brand_introduction
        if self.device is not None:
            result['Device'] = self.device
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.product_introduction is not None:
            result['ProductIntroduction'] = self.product_introduction
        if self.product_logo is not None:
            result['ProductLogo'] = self.product_logo
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_tag is not None:
            result['ProductTag'] = self.product_tag
        if self.product_website is not None:
            result['ProductWebsite'] = self.product_website
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandIntroduction') is not None:
            self.brand_introduction = m.get('BrandIntroduction')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('ProductIntroduction') is not None:
            self.product_introduction = m.get('ProductIntroduction')
        if m.get('ProductLogo') is not None:
            self.product_logo = m.get('ProductLogo')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductTag') is not None:
            self.product_tag = m.get('ProductTag')
        if m.get('ProductWebsite') is not None:
            self.product_website = m.get('ProductWebsite')
        return self


class GetOcProductBandResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcProductBandResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcProductBandResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcProductBandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcProductBandResponseBody = None,
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
            temp_model = GetOcProductBandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcTaxAbnormalRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcTaxAbnormalResponseBodyData(TeaModel):
    def __init__(
        self,
        card_num: str = None,
        card_type: str = None,
        ent_name: str = None,
        judge_date: str = None,
        judge_department: str = None,
        judge_reason: str = None,
        legal_name: str = None,
        overdue_amount: str = None,
        overdue_type: str = None,
        status: str = None,
        taxpayer_num: str = None,
    ):
        self.card_num = card_num
        self.card_type = card_type
        self.ent_name = ent_name
        self.judge_date = judge_date
        self.judge_department = judge_department
        self.judge_reason = judge_reason
        self.legal_name = legal_name
        self.overdue_amount = overdue_amount
        self.overdue_type = overdue_type
        self.status = status
        self.taxpayer_num = taxpayer_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_num is not None:
            result['CardNum'] = self.card_num
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.judge_date is not None:
            result['JudgeDate'] = self.judge_date
        if self.judge_department is not None:
            result['JudgeDepartment'] = self.judge_department
        if self.judge_reason is not None:
            result['JudgeReason'] = self.judge_reason
        if self.legal_name is not None:
            result['LegalName'] = self.legal_name
        if self.overdue_amount is not None:
            result['OverdueAmount'] = self.overdue_amount
        if self.overdue_type is not None:
            result['OverdueType'] = self.overdue_type
        if self.status is not None:
            result['Status'] = self.status
        if self.taxpayer_num is not None:
            result['TaxpayerNum'] = self.taxpayer_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardNum') is not None:
            self.card_num = m.get('CardNum')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('JudgeDate') is not None:
            self.judge_date = m.get('JudgeDate')
        if m.get('JudgeDepartment') is not None:
            self.judge_department = m.get('JudgeDepartment')
        if m.get('JudgeReason') is not None:
            self.judge_reason = m.get('JudgeReason')
        if m.get('LegalName') is not None:
            self.legal_name = m.get('LegalName')
        if m.get('OverdueAmount') is not None:
            self.overdue_amount = m.get('OverdueAmount')
        if m.get('OverdueType') is not None:
            self.overdue_type = m.get('OverdueType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaxpayerNum') is not None:
            self.taxpayer_num = m.get('TaxpayerNum')
        return self


class GetOcTaxAbnormalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcTaxAbnormalResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcTaxAbnormalResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcTaxAbnormalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcTaxAbnormalResponseBody = None,
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
            temp_model = GetOcTaxAbnormalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcTaxClassARequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcTaxClassAResponseBodyData(TeaModel):
    def __init__(
        self,
        ent_name: str = None,
        tax_level: str = None,
        taxpayer_num: str = None,
        year: str = None,
    ):
        self.ent_name = ent_name
        self.tax_level = tax_level
        self.taxpayer_num = taxpayer_num
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.tax_level is not None:
            result['TaxLevel'] = self.tax_level
        if self.taxpayer_num is not None:
            result['TaxpayerNum'] = self.taxpayer_num
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('TaxLevel') is not None:
            self.tax_level = m.get('TaxLevel')
        if m.get('TaxpayerNum') is not None:
            self.taxpayer_num = m.get('TaxpayerNum')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class GetOcTaxClassAResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcTaxClassAResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcTaxClassAResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcTaxClassAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcTaxClassAResponseBody = None,
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
            temp_model = GetOcTaxClassAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcTaxGeneralTaxpayerRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcTaxGeneralTaxpayerResponseBodyData(TeaModel):
    def __init__(
        self,
        department: str = None,
        end_date: str = None,
        ent_name: str = None,
        judge_date: str = None,
        qualification: str = None,
        start_date: str = None,
        taxpayer_num: str = None,
    ):
        self.department = department
        self.end_date = end_date
        self.ent_name = ent_name
        self.judge_date = judge_date
        self.qualification = qualification
        self.start_date = start_date
        self.taxpayer_num = taxpayer_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department is not None:
            result['Department'] = self.department
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.judge_date is not None:
            result['JudgeDate'] = self.judge_date
        if self.qualification is not None:
            result['Qualification'] = self.qualification
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.taxpayer_num is not None:
            result['TaxpayerNum'] = self.taxpayer_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('JudgeDate') is not None:
            self.judge_date = m.get('JudgeDate')
        if m.get('Qualification') is not None:
            self.qualification = m.get('Qualification')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TaxpayerNum') is not None:
            self.taxpayer_num = m.get('TaxpayerNum')
        return self


class GetOcTaxGeneralTaxpayerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcTaxGeneralTaxpayerResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcTaxGeneralTaxpayerResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcTaxGeneralTaxpayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcTaxGeneralTaxpayerResponseBody = None,
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
            temp_model = GetOcTaxGeneralTaxpayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcTaxIllegalRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcTaxIllegalResponseBodyData(TeaModel):
    def __init__(
        self,
        agency_card_num: str = None,
        agency_card_type: str = None,
        agency_ent: str = None,
        agency_name: str = None,
        agency_sex: str = None,
        case_type: str = None,
        department: str = None,
        ent_address: str = None,
        ent_name: str = None,
        financial_card_num: str = None,
        financial_card_type: str = None,
        financial_name: str = None,
        financial_sex: str = None,
        illegal_truth: str = None,
        law_basis: str = None,
        legal_card_num: str = None,
        legal_card_type: str = None,
        legal_name: str = None,
        legal_sex: str = None,
        org_code: str = None,
        publish_date: str = None,
        taxpayer_num: str = None,
    ):
        self.agency_card_num = agency_card_num
        self.agency_card_type = agency_card_type
        self.agency_ent = agency_ent
        self.agency_name = agency_name
        self.agency_sex = agency_sex
        self.case_type = case_type
        self.department = department
        self.ent_address = ent_address
        self.ent_name = ent_name
        self.financial_card_num = financial_card_num
        self.financial_card_type = financial_card_type
        self.financial_name = financial_name
        self.financial_sex = financial_sex
        self.illegal_truth = illegal_truth
        self.law_basis = law_basis
        self.legal_card_num = legal_card_num
        self.legal_card_type = legal_card_type
        self.legal_name = legal_name
        self.legal_sex = legal_sex
        self.org_code = org_code
        self.publish_date = publish_date
        self.taxpayer_num = taxpayer_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agency_card_num is not None:
            result['AgencyCardNum'] = self.agency_card_num
        if self.agency_card_type is not None:
            result['AgencyCardType'] = self.agency_card_type
        if self.agency_ent is not None:
            result['AgencyEnt'] = self.agency_ent
        if self.agency_name is not None:
            result['AgencyName'] = self.agency_name
        if self.agency_sex is not None:
            result['AgencySex'] = self.agency_sex
        if self.case_type is not None:
            result['CaseType'] = self.case_type
        if self.department is not None:
            result['Department'] = self.department
        if self.ent_address is not None:
            result['EntAddress'] = self.ent_address
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.financial_card_num is not None:
            result['FinancialCardNum'] = self.financial_card_num
        if self.financial_card_type is not None:
            result['FinancialCardType'] = self.financial_card_type
        if self.financial_name is not None:
            result['FinancialName'] = self.financial_name
        if self.financial_sex is not None:
            result['FinancialSex'] = self.financial_sex
        if self.illegal_truth is not None:
            result['IllegalTruth'] = self.illegal_truth
        if self.law_basis is not None:
            result['LawBasis'] = self.law_basis
        if self.legal_card_num is not None:
            result['LegalCardNum'] = self.legal_card_num
        if self.legal_card_type is not None:
            result['LegalCardType'] = self.legal_card_type
        if self.legal_name is not None:
            result['LegalName'] = self.legal_name
        if self.legal_sex is not None:
            result['LegalSex'] = self.legal_sex
        if self.org_code is not None:
            result['OrgCode'] = self.org_code
        if self.publish_date is not None:
            result['PublishDate'] = self.publish_date
        if self.taxpayer_num is not None:
            result['TaxpayerNum'] = self.taxpayer_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgencyCardNum') is not None:
            self.agency_card_num = m.get('AgencyCardNum')
        if m.get('AgencyCardType') is not None:
            self.agency_card_type = m.get('AgencyCardType')
        if m.get('AgencyEnt') is not None:
            self.agency_ent = m.get('AgencyEnt')
        if m.get('AgencyName') is not None:
            self.agency_name = m.get('AgencyName')
        if m.get('AgencySex') is not None:
            self.agency_sex = m.get('AgencySex')
        if m.get('CaseType') is not None:
            self.case_type = m.get('CaseType')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('EntAddress') is not None:
            self.ent_address = m.get('EntAddress')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('FinancialCardNum') is not None:
            self.financial_card_num = m.get('FinancialCardNum')
        if m.get('FinancialCardType') is not None:
            self.financial_card_type = m.get('FinancialCardType')
        if m.get('FinancialName') is not None:
            self.financial_name = m.get('FinancialName')
        if m.get('FinancialSex') is not None:
            self.financial_sex = m.get('FinancialSex')
        if m.get('IllegalTruth') is not None:
            self.illegal_truth = m.get('IllegalTruth')
        if m.get('LawBasis') is not None:
            self.law_basis = m.get('LawBasis')
        if m.get('LegalCardNum') is not None:
            self.legal_card_num = m.get('LegalCardNum')
        if m.get('LegalCardType') is not None:
            self.legal_card_type = m.get('LegalCardType')
        if m.get('LegalName') is not None:
            self.legal_name = m.get('LegalName')
        if m.get('LegalSex') is not None:
            self.legal_sex = m.get('LegalSex')
        if m.get('OrgCode') is not None:
            self.org_code = m.get('OrgCode')
        if m.get('PublishDate') is not None:
            self.publish_date = m.get('PublishDate')
        if m.get('TaxpayerNum') is not None:
            self.taxpayer_num = m.get('TaxpayerNum')
        return self


class GetOcTaxIllegalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcTaxIllegalResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcTaxIllegalResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcTaxIllegalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcTaxIllegalResponseBody = None,
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
            temp_model = GetOcTaxIllegalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcTaxOverdueRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcTaxOverdueResponseBodyData(TeaModel):
    def __init__(
        self,
        curr_overdue_amount: str = None,
        department: str = None,
        ent_address: str = None,
        ent_name: str = None,
        legal_name: str = None,
        overdue_amount: str = None,
        overdue_type: str = None,
        publish_date: str = None,
        taxpayer_num: str = None,
        taxpayer_type: str = None,
    ):
        self.curr_overdue_amount = curr_overdue_amount
        self.department = department
        self.ent_address = ent_address
        self.ent_name = ent_name
        self.legal_name = legal_name
        self.overdue_amount = overdue_amount
        self.overdue_type = overdue_type
        self.publish_date = publish_date
        self.taxpayer_num = taxpayer_num
        self.taxpayer_type = taxpayer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_overdue_amount is not None:
            result['CurrOverdueAmount'] = self.curr_overdue_amount
        if self.department is not None:
            result['Department'] = self.department
        if self.ent_address is not None:
            result['EntAddress'] = self.ent_address
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.legal_name is not None:
            result['LegalName'] = self.legal_name
        if self.overdue_amount is not None:
            result['OverdueAmount'] = self.overdue_amount
        if self.overdue_type is not None:
            result['OverdueType'] = self.overdue_type
        if self.publish_date is not None:
            result['PublishDate'] = self.publish_date
        if self.taxpayer_num is not None:
            result['TaxpayerNum'] = self.taxpayer_num
        if self.taxpayer_type is not None:
            result['TaxpayerType'] = self.taxpayer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrOverdueAmount') is not None:
            self.curr_overdue_amount = m.get('CurrOverdueAmount')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('EntAddress') is not None:
            self.ent_address = m.get('EntAddress')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('LegalName') is not None:
            self.legal_name = m.get('LegalName')
        if m.get('OverdueAmount') is not None:
            self.overdue_amount = m.get('OverdueAmount')
        if m.get('OverdueType') is not None:
            self.overdue_type = m.get('OverdueType')
        if m.get('PublishDate') is not None:
            self.publish_date = m.get('PublishDate')
        if m.get('TaxpayerNum') is not None:
            self.taxpayer_num = m.get('TaxpayerNum')
        if m.get('TaxpayerType') is not None:
            self.taxpayer_type = m.get('TaxpayerType')
        return self


class GetOcTaxOverdueResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcTaxOverdueResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcTaxOverdueResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcTaxOverdueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcTaxOverdueResponseBody = None,
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
            temp_model = GetOcTaxOverdueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOcTaxPunishmentRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetOcTaxPunishmentResponseBodyData(TeaModel):
    def __init__(
        self,
        department: str = None,
        ent_name: str = None,
        event_name: str = None,
        event_type: str = None,
        legal_name: str = None,
        punish_date: str = None,
        taxpayer_num: str = None,
        title: str = None,
    ):
        self.department = department
        self.ent_name = ent_name
        self.event_name = event_name
        self.event_type = event_type
        self.legal_name = legal_name
        self.punish_date = punish_date
        self.taxpayer_num = taxpayer_num
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department is not None:
            result['Department'] = self.department
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.legal_name is not None:
            result['LegalName'] = self.legal_name
        if self.punish_date is not None:
            result['PunishDate'] = self.punish_date
        if self.taxpayer_num is not None:
            result['TaxpayerNum'] = self.taxpayer_num
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('LegalName') is not None:
            self.legal_name = m.get('LegalName')
        if m.get('PunishDate') is not None:
            self.punish_date = m.get('PunishDate')
        if m.get('TaxpayerNum') is not None:
            self.taxpayer_num = m.get('TaxpayerNum')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetOcTaxPunishmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOcTaxPunishmentResponseBodyData] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOcTaxPunishmentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetOcTaxPunishmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOcTaxPunishmentResponseBody = None,
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
            temp_model = GetOcTaxPunishmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQccCertificationDetailByIdRequest(TeaModel):
    def __init__(
        self,
        cert_id: str = None,
    ):
        self.cert_id = cert_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        return self


class GetQccCertificationDetailByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

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
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetQccCertificationDetailByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQccCertificationDetailByIdResponseBody = None,
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
            temp_model = GetQccCertificationDetailByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQccSearchCertificationRequest(TeaModel):
    def __init__(
        self,
        cert_category: str = None,
        ent_name: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.cert_category = cert_category
        self.ent_name = ent_name
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_category is not None:
            result['CertCategory'] = self.cert_category
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCategory') is not None:
            self.cert_category = m.get('CertCategory')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetQccSearchCertificationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[Dict[str, Any]] = None,
        message: str = None,
        page_index: int = None,
        page_num: int = None,
        request_id: str = None,
        success: bool = None,
        total_num: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_index = page_index
        self.page_num = page_num
        self.request_id = request_id
        self.success = success
        self.total_num = total_num

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
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetQccSearchCertificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQccSearchCertificationResponseBody = None,
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
            temp_model = GetQccSearchCertificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


