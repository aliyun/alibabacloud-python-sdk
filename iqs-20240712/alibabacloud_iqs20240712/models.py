# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AgentBaseQuery(TeaModel):
    def __init__(
        self,
        query: str = None,
    ):
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class QueryResultDataImages(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class QueryResultDataMetadata(TeaModel):
    def __init__(
        self,
        business_area: str = None,
        daily_opening_hours: str = None,
        main_tag: str = None,
        phone: str = None,
        score: str = None,
        weekly_opening_days: str = None,
    ):
        self.business_area = business_area
        self.daily_opening_hours = daily_opening_hours
        self.main_tag = main_tag
        self.phone = phone
        self.score = score
        self.weekly_opening_days = weekly_opening_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_area is not None:
            result['businessArea'] = self.business_area
        if self.daily_opening_hours is not None:
            result['dailyOpeningHours'] = self.daily_opening_hours
        if self.main_tag is not None:
            result['mainTag'] = self.main_tag
        if self.phone is not None:
            result['phone'] = self.phone
        if self.score is not None:
            result['score'] = self.score
        if self.weekly_opening_days is not None:
            result['weeklyOpeningDays'] = self.weekly_opening_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessArea') is not None:
            self.business_area = m.get('businessArea')
        if m.get('dailyOpeningHours') is not None:
            self.daily_opening_hours = m.get('dailyOpeningHours')
        if m.get('mainTag') is not None:
            self.main_tag = m.get('mainTag')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('weeklyOpeningDays') is not None:
            self.weekly_opening_days = m.get('weeklyOpeningDays')
        return self


class QueryResultData(TeaModel):
    def __init__(
        self,
        address: str = None,
        city_code: str = None,
        city_name: str = None,
        district_code: str = None,
        district_name: str = None,
        id: str = None,
        images: List[QueryResultDataImages] = None,
        latitude: str = None,
        longitude: str = None,
        metadata: QueryResultDataMetadata = None,
        name: str = None,
        province_code: str = None,
        province_name: str = None,
        type_code: str = None,
        types: str = None,
    ):
        self.address = address
        self.city_code = city_code
        self.city_name = city_name
        self.district_code = district_code
        self.district_name = district_name
        self.id = id
        self.images = images
        self.latitude = latitude
        self.longitude = longitude
        self.metadata = metadata
        self.name = name
        self.province_code = province_code
        self.province_name = province_name
        self.type_code = type_code
        self.types = types

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.city_code is not None:
            result['cityCode'] = self.city_code
        if self.city_name is not None:
            result['cityName'] = self.city_name
        if self.district_code is not None:
            result['districtCode'] = self.district_code
        if self.district_name is not None:
            result['districtName'] = self.district_name
        if self.id is not None:
            result['id'] = self.id
        result['images'] = []
        if self.images is not None:
            for k in self.images:
                result['images'].append(k.to_map() if k else None)
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.province_code is not None:
            result['provinceCode'] = self.province_code
        if self.province_name is not None:
            result['provinceName'] = self.province_name
        if self.type_code is not None:
            result['typeCode'] = self.type_code
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('cityCode') is not None:
            self.city_code = m.get('cityCode')
        if m.get('cityName') is not None:
            self.city_name = m.get('cityName')
        if m.get('districtCode') is not None:
            self.district_code = m.get('districtCode')
        if m.get('districtName') is not None:
            self.district_name = m.get('districtName')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.images = []
        if m.get('images') is not None:
            for k in m.get('images'):
                temp_model = QueryResultDataImages()
                self.images.append(temp_model.from_map(k))
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('metadata') is not None:
            temp_model = QueryResultDataMetadata()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provinceCode') is not None:
            self.province_code = m.get('provinceCode')
        if m.get('provinceName') is not None:
            self.province_name = m.get('provinceName')
        if m.get('typeCode') is not None:
            self.type_code = m.get('typeCode')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class QueryResult(TeaModel):
    def __init__(
        self,
        data: List[QueryResultData] = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = QueryResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryAttractionsRequest(TeaModel):
    def __init__(
        self,
        body: AgentBaseQuery = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AgentBaseQuery()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAttractionsResponseBody(TeaModel):
    def __init__(
        self,
        query_result: QueryResult = None,
        request_id: str = None,
    ):
        self.query_result = query_result
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.query_result:
            self.query_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_result is not None:
            result['queryResult'] = self.query_result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryResult') is not None:
            temp_model = QueryResult()
            self.query_result = temp_model.from_map(m['queryResult'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryAttractionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAttractionsResponseBody = None,
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
            temp_model = QueryAttractionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHotelsRequest(TeaModel):
    def __init__(
        self,
        body: AgentBaseQuery = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AgentBaseQuery()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHotelsResponseBody(TeaModel):
    def __init__(
        self,
        query_result: QueryResult = None,
        request_id: str = None,
    ):
        self.query_result = query_result
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.query_result:
            self.query_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_result is not None:
            result['queryResult'] = self.query_result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryResult') is not None:
            temp_model = QueryResult()
            self.query_result = temp_model.from_map(m['queryResult'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryHotelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryHotelsResponseBody = None,
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
            temp_model = QueryHotelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRestaurantsRequest(TeaModel):
    def __init__(
        self,
        body: AgentBaseQuery = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AgentBaseQuery()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRestaurantsResponseBody(TeaModel):
    def __init__(
        self,
        query_result: QueryResult = None,
        request_id: str = None,
    ):
        self.query_result = query_result
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.query_result:
            self.query_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_result is not None:
            result['queryResult'] = self.query_result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryResult') is not None:
            temp_model = QueryResult()
            self.query_result = temp_model.from_map(m['queryResult'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryRestaurantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRestaurantsResponseBody = None,
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
            temp_model = QueryRestaurantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


