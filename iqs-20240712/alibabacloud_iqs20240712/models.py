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


class CommonAgentQuery(TeaModel):
    def __init__(
        self,
        limit: int = None,
        query: str = None,
        query_scene_enum_code: str = None,
        search_model: str = None,
    ):
        self.limit = limit
        self.query = query
        self.query_scene_enum_code = query_scene_enum_code
        self.search_model = search_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.query is not None:
            result['query'] = self.query
        if self.query_scene_enum_code is not None:
            result['querySceneEnumCode'] = self.query_scene_enum_code
        if self.search_model is not None:
            result['searchModel'] = self.search_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('querySceneEnumCode') is not None:
            self.query_scene_enum_code = m.get('querySceneEnumCode')
        if m.get('searchModel') is not None:
            self.search_model = m.get('searchModel')
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
        average_spend: str = None,
        business_area: str = None,
        daily_opening_hours: str = None,
        main_tag: str = None,
        phone: str = None,
        score: str = None,
        weekly_opening_days: str = None,
    ):
        self.average_spend = average_spend
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
        if self.average_spend is not None:
            result['averageSpend'] = self.average_spend
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
        if m.get('averageSpend') is not None:
            self.average_spend = m.get('averageSpend')
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
        distance_meter: str = None,
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
        self.distance_meter = distance_meter
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
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
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
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
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
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = QueryResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class BicyclingDirectionNovaRequest(TeaModel):
    def __init__(
        self,
        destination_latitude: str = None,
        destination_longitude: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
        show_polyline: bool = None,
    ):
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.show_polyline = show_polyline

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        if self.show_polyline is not None:
            result['showPolyline'] = self.show_polyline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        if m.get('showPolyline') is not None:
            self.show_polyline = m.get('showPolyline')
        return self


class BicyclingDirectionNovaResponseBodyDataPathsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class BicyclingDirectionNovaResponseBodyDataPathsStepsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class BicyclingDirectionNovaResponseBodyDataPathsSteps(TeaModel):
    def __init__(
        self,
        cost: BicyclingDirectionNovaResponseBodyDataPathsStepsCost = None,
        instruction: str = None,
        orientation: str = None,
        polyline: str = None,
        road_name: str = None,
        step_distance_meter: str = None,
    ):
        self.cost = cost
        self.instruction = instruction
        self.orientation = orientation
        self.polyline = polyline
        self.road_name = road_name
        self.step_distance_meter = step_distance_meter

    def validate(self):
        if self.cost:
            self.cost.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.instruction is not None:
            result['instruction'] = self.instruction
        if self.orientation is not None:
            result['orientation'] = self.orientation
        if self.polyline is not None:
            result['polyline'] = self.polyline
        if self.road_name is not None:
            result['roadName'] = self.road_name
        if self.step_distance_meter is not None:
            result['stepDistanceMeter'] = self.step_distance_meter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = BicyclingDirectionNovaResponseBodyDataPathsStepsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')
        if m.get('orientation') is not None:
            self.orientation = m.get('orientation')
        if m.get('polyline') is not None:
            self.polyline = m.get('polyline')
        if m.get('roadName') is not None:
            self.road_name = m.get('roadName')
        if m.get('stepDistanceMeter') is not None:
            self.step_distance_meter = m.get('stepDistanceMeter')
        return self


class BicyclingDirectionNovaResponseBodyDataPaths(TeaModel):
    def __init__(
        self,
        cost: BicyclingDirectionNovaResponseBodyDataPathsCost = None,
        distance_meter: str = None,
        duration_second: str = None,
        restriction: str = None,
        steps: List[BicyclingDirectionNovaResponseBodyDataPathsSteps] = None,
    ):
        self.cost = cost
        self.distance_meter = distance_meter
        self.duration_second = duration_second
        self.restriction = restriction
        self.steps = steps

    def validate(self):
        if self.cost:
            self.cost.validate()
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.restriction is not None:
            result['restriction'] = self.restriction
        result['steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['steps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = BicyclingDirectionNovaResponseBodyDataPathsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('restriction') is not None:
            self.restriction = m.get('restriction')
        self.steps = []
        if m.get('steps') is not None:
            for k in m.get('steps'):
                temp_model = BicyclingDirectionNovaResponseBodyDataPathsSteps()
                self.steps.append(temp_model.from_map(k))
        return self


class BicyclingDirectionNovaResponseBodyData(TeaModel):
    def __init__(
        self,
        count: str = None,
        destination_latitude: str = None,
        destination_longitude: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
        paths: List[BicyclingDirectionNovaResponseBodyDataPaths] = None,
        taxi_cost: str = None,
    ):
        self.count = count
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.paths = paths
        self.taxi_cost = taxi_cost

    def validate(self):
        if self.paths:
            for k in self.paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        result['paths'] = []
        if self.paths is not None:
            for k in self.paths:
                result['paths'].append(k.to_map() if k else None)
        if self.taxi_cost is not None:
            result['taxiCost'] = self.taxi_cost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        self.paths = []
        if m.get('paths') is not None:
            for k in m.get('paths'):
                temp_model = BicyclingDirectionNovaResponseBodyDataPaths()
                self.paths.append(temp_model.from_map(k))
        if m.get('taxiCost') is not None:
            self.taxi_cost = m.get('taxiCost')
        return self


class BicyclingDirectionNovaResponseBody(TeaModel):
    def __init__(
        self,
        data: BicyclingDirectionNovaResponseBodyData = None,
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
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = BicyclingDirectionNovaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class BicyclingDirectionNovaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BicyclingDirectionNovaResponseBody = None,
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
            temp_model = BicyclingDirectionNovaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommonQueryBySceneRequest(TeaModel):
    def __init__(
        self,
        body: CommonAgentQuery = None,
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
            temp_model = CommonAgentQuery()
            self.body = temp_model.from_map(m['body'])
        return self


class CommonQueryBySceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryResult = None,
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
            temp_model = QueryResult()
            self.body = temp_model.from_map(m['body'])
        return self


class DrivingDirectionRequest(TeaModel):
    def __init__(
        self,
        destination_latitude: str = None,
        destination_longitude: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
    ):
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        return self


class DrivingDirectionResponseBodyDataCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class DrivingDirectionResponseBodyDataStepsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class DrivingDirectionResponseBodyDataSteps(TeaModel):
    def __init__(
        self,
        cost: DrivingDirectionResponseBodyDataStepsCost = None,
        instruction: str = None,
        orientation: str = None,
        road_name: str = None,
        step_distance_meter: str = None,
    ):
        self.cost = cost
        self.instruction = instruction
        self.orientation = orientation
        self.road_name = road_name
        self.step_distance_meter = step_distance_meter

    def validate(self):
        if self.cost:
            self.cost.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.instruction is not None:
            result['instruction'] = self.instruction
        if self.orientation is not None:
            result['orientation'] = self.orientation
        if self.road_name is not None:
            result['roadName'] = self.road_name
        if self.step_distance_meter is not None:
            result['stepDistanceMeter'] = self.step_distance_meter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = DrivingDirectionResponseBodyDataStepsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')
        if m.get('orientation') is not None:
            self.orientation = m.get('orientation')
        if m.get('roadName') is not None:
            self.road_name = m.get('roadName')
        if m.get('stepDistanceMeter') is not None:
            self.step_distance_meter = m.get('stepDistanceMeter')
        return self


class DrivingDirectionResponseBodyData(TeaModel):
    def __init__(
        self,
        cost: DrivingDirectionResponseBodyDataCost = None,
        distance_meter: str = None,
        restriction: str = None,
        steps: List[DrivingDirectionResponseBodyDataSteps] = None,
    ):
        self.cost = cost
        self.distance_meter = distance_meter
        self.restriction = restriction
        self.steps = steps

    def validate(self):
        if self.cost:
            self.cost.validate()
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.restriction is not None:
            result['restriction'] = self.restriction
        result['steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['steps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = DrivingDirectionResponseBodyDataCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('restriction') is not None:
            self.restriction = m.get('restriction')
        self.steps = []
        if m.get('steps') is not None:
            for k in m.get('steps'):
                temp_model = DrivingDirectionResponseBodyDataSteps()
                self.steps.append(temp_model.from_map(k))
        return self


class DrivingDirectionResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DrivingDirectionResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = DrivingDirectionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DrivingDirectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DrivingDirectionResponseBody = None,
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
            temp_model = DrivingDirectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DrivingDirectionNovaRequest(TeaModel):
    def __init__(
        self,
        car_type: str = None,
        destination_latitude: str = None,
        destination_longitude: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
        plate: str = None,
        show_polyline: bool = None,
    ):
        self.car_type = car_type
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.plate = plate
        self.show_polyline = show_polyline

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.car_type is not None:
            result['carType'] = self.car_type
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        if self.plate is not None:
            result['plate'] = self.plate
        if self.show_polyline is not None:
            result['showPolyline'] = self.show_polyline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carType') is not None:
            self.car_type = m.get('carType')
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        if m.get('plate') is not None:
            self.plate = m.get('plate')
        if m.get('showPolyline') is not None:
            self.show_polyline = m.get('showPolyline')
        return self


class DrivingDirectionNovaResponseBodyDataPathsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class DrivingDirectionNovaResponseBodyDataPathsStepsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class DrivingDirectionNovaResponseBodyDataPathsSteps(TeaModel):
    def __init__(
        self,
        cost: DrivingDirectionNovaResponseBodyDataPathsStepsCost = None,
        instruction: str = None,
        orientation: str = None,
        polyline: str = None,
        road_name: str = None,
        step_distance_meter: str = None,
    ):
        self.cost = cost
        self.instruction = instruction
        self.orientation = orientation
        self.polyline = polyline
        self.road_name = road_name
        self.step_distance_meter = step_distance_meter

    def validate(self):
        if self.cost:
            self.cost.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.instruction is not None:
            result['instruction'] = self.instruction
        if self.orientation is not None:
            result['orientation'] = self.orientation
        if self.polyline is not None:
            result['polyline'] = self.polyline
        if self.road_name is not None:
            result['roadName'] = self.road_name
        if self.step_distance_meter is not None:
            result['stepDistanceMeter'] = self.step_distance_meter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = DrivingDirectionNovaResponseBodyDataPathsStepsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')
        if m.get('orientation') is not None:
            self.orientation = m.get('orientation')
        if m.get('polyline') is not None:
            self.polyline = m.get('polyline')
        if m.get('roadName') is not None:
            self.road_name = m.get('roadName')
        if m.get('stepDistanceMeter') is not None:
            self.step_distance_meter = m.get('stepDistanceMeter')
        return self


class DrivingDirectionNovaResponseBodyDataPaths(TeaModel):
    def __init__(
        self,
        cost: DrivingDirectionNovaResponseBodyDataPathsCost = None,
        distance_meter: str = None,
        duration_second: str = None,
        restriction: str = None,
        steps: List[DrivingDirectionNovaResponseBodyDataPathsSteps] = None,
    ):
        self.cost = cost
        self.distance_meter = distance_meter
        self.duration_second = duration_second
        self.restriction = restriction
        self.steps = steps

    def validate(self):
        if self.cost:
            self.cost.validate()
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.restriction is not None:
            result['restriction'] = self.restriction
        result['steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['steps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = DrivingDirectionNovaResponseBodyDataPathsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('restriction') is not None:
            self.restriction = m.get('restriction')
        self.steps = []
        if m.get('steps') is not None:
            for k in m.get('steps'):
                temp_model = DrivingDirectionNovaResponseBodyDataPathsSteps()
                self.steps.append(temp_model.from_map(k))
        return self


class DrivingDirectionNovaResponseBodyData(TeaModel):
    def __init__(
        self,
        count: str = None,
        destination_latitude: str = None,
        destination_longitude: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
        paths: List[DrivingDirectionNovaResponseBodyDataPaths] = None,
        taxi_cost: str = None,
    ):
        self.count = count
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.paths = paths
        self.taxi_cost = taxi_cost

    def validate(self):
        if self.paths:
            for k in self.paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        result['paths'] = []
        if self.paths is not None:
            for k in self.paths:
                result['paths'].append(k.to_map() if k else None)
        if self.taxi_cost is not None:
            result['taxiCost'] = self.taxi_cost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        self.paths = []
        if m.get('paths') is not None:
            for k in m.get('paths'):
                temp_model = DrivingDirectionNovaResponseBodyDataPaths()
                self.paths.append(temp_model.from_map(k))
        if m.get('taxiCost') is not None:
            self.taxi_cost = m.get('taxiCost')
        return self


class DrivingDirectionNovaResponseBody(TeaModel):
    def __init__(
        self,
        data: DrivingDirectionNovaResponseBodyData = None,
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
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DrivingDirectionNovaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DrivingDirectionNovaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DrivingDirectionNovaResponseBody = None,
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
            temp_model = DrivingDirectionNovaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ElectrobikeDirectionNovaRequest(TeaModel):
    def __init__(
        self,
        destination_latitude: str = None,
        destination_longitude: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
        show_polyline: bool = None,
    ):
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.show_polyline = show_polyline

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        if self.show_polyline is not None:
            result['showPolyline'] = self.show_polyline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        if m.get('showPolyline') is not None:
            self.show_polyline = m.get('showPolyline')
        return self


class ElectrobikeDirectionNovaResponseBodyDataPathsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class ElectrobikeDirectionNovaResponseBodyDataPathsStepsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class ElectrobikeDirectionNovaResponseBodyDataPathsSteps(TeaModel):
    def __init__(
        self,
        cost: ElectrobikeDirectionNovaResponseBodyDataPathsStepsCost = None,
        instruction: str = None,
        orientation: str = None,
        polyline: str = None,
        road_name: str = None,
        step_distance_meter: str = None,
    ):
        self.cost = cost
        self.instruction = instruction
        self.orientation = orientation
        self.polyline = polyline
        self.road_name = road_name
        self.step_distance_meter = step_distance_meter

    def validate(self):
        if self.cost:
            self.cost.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.instruction is not None:
            result['instruction'] = self.instruction
        if self.orientation is not None:
            result['orientation'] = self.orientation
        if self.polyline is not None:
            result['polyline'] = self.polyline
        if self.road_name is not None:
            result['roadName'] = self.road_name
        if self.step_distance_meter is not None:
            result['stepDistanceMeter'] = self.step_distance_meter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = ElectrobikeDirectionNovaResponseBodyDataPathsStepsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')
        if m.get('orientation') is not None:
            self.orientation = m.get('orientation')
        if m.get('polyline') is not None:
            self.polyline = m.get('polyline')
        if m.get('roadName') is not None:
            self.road_name = m.get('roadName')
        if m.get('stepDistanceMeter') is not None:
            self.step_distance_meter = m.get('stepDistanceMeter')
        return self


class ElectrobikeDirectionNovaResponseBodyDataPaths(TeaModel):
    def __init__(
        self,
        cost: ElectrobikeDirectionNovaResponseBodyDataPathsCost = None,
        distance_meter: str = None,
        duration_second: str = None,
        restriction: str = None,
        steps: List[ElectrobikeDirectionNovaResponseBodyDataPathsSteps] = None,
    ):
        self.cost = cost
        self.distance_meter = distance_meter
        self.duration_second = duration_second
        self.restriction = restriction
        self.steps = steps

    def validate(self):
        if self.cost:
            self.cost.validate()
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.restriction is not None:
            result['restriction'] = self.restriction
        result['steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['steps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = ElectrobikeDirectionNovaResponseBodyDataPathsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('restriction') is not None:
            self.restriction = m.get('restriction')
        self.steps = []
        if m.get('steps') is not None:
            for k in m.get('steps'):
                temp_model = ElectrobikeDirectionNovaResponseBodyDataPathsSteps()
                self.steps.append(temp_model.from_map(k))
        return self


class ElectrobikeDirectionNovaResponseBodyData(TeaModel):
    def __init__(
        self,
        count: str = None,
        destination_latitude: str = None,
        destination_longitude: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
        paths: List[ElectrobikeDirectionNovaResponseBodyDataPaths] = None,
        taxi_cost: str = None,
    ):
        self.count = count
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.paths = paths
        self.taxi_cost = taxi_cost

    def validate(self):
        if self.paths:
            for k in self.paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        result['paths'] = []
        if self.paths is not None:
            for k in self.paths:
                result['paths'].append(k.to_map() if k else None)
        if self.taxi_cost is not None:
            result['taxiCost'] = self.taxi_cost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        self.paths = []
        if m.get('paths') is not None:
            for k in m.get('paths'):
                temp_model = ElectrobikeDirectionNovaResponseBodyDataPaths()
                self.paths.append(temp_model.from_map(k))
        if m.get('taxiCost') is not None:
            self.taxi_cost = m.get('taxiCost')
        return self


class ElectrobikeDirectionNovaResponseBody(TeaModel):
    def __init__(
        self,
        data: ElectrobikeDirectionNovaResponseBodyData = None,
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
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ElectrobikeDirectionNovaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ElectrobikeDirectionNovaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ElectrobikeDirectionNovaResponseBody = None,
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
            temp_model = ElectrobikeDirectionNovaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GeoCodeRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
    ):
        self.address = address
        self.city = city

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.city is not None:
            result['city'] = self.city
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('city') is not None:
            self.city = m.get('city')
        return self


class GeoCodeResponseBodyDataBuilding(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GeoCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        building: GeoCodeResponseBodyDataBuilding = None,
        city: str = None,
        city_code: str = None,
        district: str = None,
        district_code: str = None,
        latitude: str = None,
        level: str = None,
        longitude: str = None,
        number: str = None,
        province: str = None,
        street: str = None,
    ):
        self.building = building
        self.city = city
        self.city_code = city_code
        self.district = district
        self.district_code = district_code
        self.latitude = latitude
        self.level = level
        self.longitude = longitude
        self.number = number
        self.province = province
        self.street = street

    def validate(self):
        if self.building:
            self.building.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.building is not None:
            result['building'] = self.building.to_map()
        if self.city is not None:
            result['city'] = self.city
        if self.city_code is not None:
            result['cityCode'] = self.city_code
        if self.district is not None:
            result['district'] = self.district
        if self.district_code is not None:
            result['districtCode'] = self.district_code
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.level is not None:
            result['level'] = self.level
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.number is not None:
            result['number'] = self.number
        if self.province is not None:
            result['province'] = self.province
        if self.street is not None:
            result['street'] = self.street
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('building') is not None:
            temp_model = GeoCodeResponseBodyDataBuilding()
            self.building = temp_model.from_map(m['building'])
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('cityCode') is not None:
            self.city_code = m.get('cityCode')
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('districtCode') is not None:
            self.district_code = m.get('districtCode')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('street') is not None:
            self.street = m.get('street')
        return self


class GeoCodeResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GeoCodeResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GeoCodeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GeoCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GeoCodeResponseBody = None,
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
            temp_model = GeoCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NearbySearchNovaRequest(TeaModel):
    def __init__(
        self,
        city_limit: bool = None,
        keywords: str = None,
        latitude: str = None,
        longitude: str = None,
        page: int = None,
        radius: int = None,
        size: int = None,
        sort_rule: str = None,
        types: str = None,
    ):
        self.city_limit = city_limit
        self.keywords = keywords
        self.latitude = latitude
        self.longitude = longitude
        self.page = page
        self.radius = radius
        self.size = size
        self.sort_rule = sort_rule
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_limit is not None:
            result['cityLimit'] = self.city_limit
        if self.keywords is not None:
            result['keywords'] = self.keywords
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.page is not None:
            result['page'] = self.page
        if self.radius is not None:
            result['radius'] = self.radius
        if self.size is not None:
            result['size'] = self.size
        if self.sort_rule is not None:
            result['sortRule'] = self.sort_rule
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cityLimit') is not None:
            self.city_limit = m.get('cityLimit')
        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('radius') is not None:
            self.radius = m.get('radius')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('sortRule') is not None:
            self.sort_rule = m.get('sortRule')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class NearbySearchNovaResponseBodyDataImages(TeaModel):
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


class NearbySearchNovaResponseBodyDataMetadata(TeaModel):
    def __init__(
        self,
        average_spend: str = None,
        business_area: str = None,
        daily_opening_hours: str = None,
        main_tag: str = None,
        phone: str = None,
        score: str = None,
        tag: str = None,
        weekly_opening_days: str = None,
    ):
        self.average_spend = average_spend
        self.business_area = business_area
        self.daily_opening_hours = daily_opening_hours
        self.main_tag = main_tag
        self.phone = phone
        self.score = score
        self.tag = tag
        self.weekly_opening_days = weekly_opening_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_spend is not None:
            result['averageSpend'] = self.average_spend
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
        if self.tag is not None:
            result['tag'] = self.tag
        if self.weekly_opening_days is not None:
            result['weeklyOpeningDays'] = self.weekly_opening_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('averageSpend') is not None:
            self.average_spend = m.get('averageSpend')
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
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('weeklyOpeningDays') is not None:
            self.weekly_opening_days = m.get('weeklyOpeningDays')
        return self


class NearbySearchNovaResponseBodyData(TeaModel):
    def __init__(
        self,
        address: str = None,
        city_code: str = None,
        city_name: str = None,
        distance_meter: str = None,
        district_code: str = None,
        district_name: str = None,
        id: str = None,
        images: List[NearbySearchNovaResponseBodyDataImages] = None,
        latitude: str = None,
        longitude: str = None,
        metadata: NearbySearchNovaResponseBodyDataMetadata = None,
        name: str = None,
        province_code: str = None,
        province_name: str = None,
        type_code: str = None,
        types: str = None,
    ):
        self.address = address
        self.city_code = city_code
        self.city_name = city_name
        self.distance_meter = distance_meter
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
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
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
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('districtCode') is not None:
            self.district_code = m.get('districtCode')
        if m.get('districtName') is not None:
            self.district_name = m.get('districtName')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.images = []
        if m.get('images') is not None:
            for k in m.get('images'):
                temp_model = NearbySearchNovaResponseBodyDataImages()
                self.images.append(temp_model.from_map(k))
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('metadata') is not None:
            temp_model = NearbySearchNovaResponseBodyDataMetadata()
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


class NearbySearchNovaResponseBody(TeaModel):
    def __init__(
        self,
        data: List[NearbySearchNovaResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = NearbySearchNovaResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class NearbySearchNovaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NearbySearchNovaResponseBody = None,
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
            temp_model = NearbySearchNovaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PlaceSearchNovaRequest(TeaModel):
    def __init__(
        self,
        city_limit: bool = None,
        keywords: str = None,
        page: int = None,
        region: str = None,
        size: int = None,
        types: str = None,
    ):
        self.city_limit = city_limit
        self.keywords = keywords
        self.page = page
        self.region = region
        self.size = size
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_limit is not None:
            result['cityLimit'] = self.city_limit
        if self.keywords is not None:
            result['keywords'] = self.keywords
        if self.page is not None:
            result['page'] = self.page
        if self.region is not None:
            result['region'] = self.region
        if self.size is not None:
            result['size'] = self.size
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cityLimit') is not None:
            self.city_limit = m.get('cityLimit')
        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class PlaceSearchNovaResponseBodyDataImages(TeaModel):
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


class PlaceSearchNovaResponseBodyDataMetadata(TeaModel):
    def __init__(
        self,
        average_spend: str = None,
        business_area: str = None,
        daily_opening_hours: str = None,
        main_tag: str = None,
        phone: str = None,
        score: str = None,
        tag: str = None,
        weekly_opening_days: str = None,
    ):
        self.average_spend = average_spend
        self.business_area = business_area
        self.daily_opening_hours = daily_opening_hours
        self.main_tag = main_tag
        self.phone = phone
        self.score = score
        self.tag = tag
        self.weekly_opening_days = weekly_opening_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_spend is not None:
            result['averageSpend'] = self.average_spend
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
        if self.tag is not None:
            result['tag'] = self.tag
        if self.weekly_opening_days is not None:
            result['weeklyOpeningDays'] = self.weekly_opening_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('averageSpend') is not None:
            self.average_spend = m.get('averageSpend')
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
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('weeklyOpeningDays') is not None:
            self.weekly_opening_days = m.get('weeklyOpeningDays')
        return self


class PlaceSearchNovaResponseBodyData(TeaModel):
    def __init__(
        self,
        address: str = None,
        city_code: str = None,
        city_name: str = None,
        distance_meter: str = None,
        district_code: str = None,
        district_name: str = None,
        id: str = None,
        images: List[PlaceSearchNovaResponseBodyDataImages] = None,
        latitude: str = None,
        longitude: str = None,
        metadata: PlaceSearchNovaResponseBodyDataMetadata = None,
        name: str = None,
        province_code: str = None,
        province_name: str = None,
        type_code: str = None,
        types: str = None,
    ):
        self.address = address
        self.city_code = city_code
        self.city_name = city_name
        self.distance_meter = distance_meter
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
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
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
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('districtCode') is not None:
            self.district_code = m.get('districtCode')
        if m.get('districtName') is not None:
            self.district_name = m.get('districtName')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.images = []
        if m.get('images') is not None:
            for k in m.get('images'):
                temp_model = PlaceSearchNovaResponseBodyDataImages()
                self.images.append(temp_model.from_map(k))
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('metadata') is not None:
            temp_model = PlaceSearchNovaResponseBodyDataMetadata()
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


class PlaceSearchNovaResponseBody(TeaModel):
    def __init__(
        self,
        data: List[PlaceSearchNovaResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = PlaceSearchNovaResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class PlaceSearchNovaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PlaceSearchNovaResponseBody = None,
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
            temp_model = PlaceSearchNovaResponseBody()
            self.body = temp_model.from_map(m['body'])
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


class QueryAttractionsNlRequest(TeaModel):
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


class QueryAttractionsNlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryResult = None,
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
            temp_model = QueryResult()
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


class QueryHotelsNlRequest(TeaModel):
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


class QueryHotelsNlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryResult = None,
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
            temp_model = QueryResult()
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


class QueryRestaurantsNlRequest(TeaModel):
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


class QueryRestaurantsNlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryResult = None,
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
            temp_model = QueryResult()
            self.body = temp_model.from_map(m['body'])
        return self


class RgeoCodeRequest(TeaModel):
    def __init__(
        self,
        latitude: str = None,
        longitude: str = None,
    ):
        self.latitude = latitude
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        return self


class RgeoCodeResponseBodyDataBuilding(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RgeoCodeResponseBodyDataBusinessAreas(TeaModel):
    def __init__(
        self,
        id: str = None,
        latitude: str = None,
        longitude: str = None,
        name: str = None,
    ):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class RgeoCodeResponseBodyDataNeighborhood(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RgeoCodeResponseBodyDataStreetNumber(TeaModel):
    def __init__(
        self,
        direction: str = None,
        distance_meter: str = None,
        latitude: str = None,
        longitude: str = None,
        number: str = None,
        street: str = None,
    ):
        self.direction = direction
        self.distance_meter = distance_meter
        self.latitude = latitude
        self.longitude = longitude
        self.number = number
        self.street = street

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['direction'] = self.direction
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.number is not None:
            result['number'] = self.number
        if self.street is not None:
            result['street'] = self.street
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('street') is not None:
            self.street = m.get('street')
        return self


class RgeoCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        building: RgeoCodeResponseBodyDataBuilding = None,
        business_areas: List[RgeoCodeResponseBodyDataBusinessAreas] = None,
        city: str = None,
        city_code: str = None,
        country: str = None,
        district: str = None,
        district_code: str = None,
        formatted_address: str = None,
        neighborhood: RgeoCodeResponseBodyDataNeighborhood = None,
        province: str = None,
        street_number: RgeoCodeResponseBodyDataStreetNumber = None,
        town_code: str = None,
        town_ship: str = None,
    ):
        self.building = building
        self.business_areas = business_areas
        self.city = city
        self.city_code = city_code
        self.country = country
        self.district = district
        self.district_code = district_code
        self.formatted_address = formatted_address
        self.neighborhood = neighborhood
        self.province = province
        self.street_number = street_number
        self.town_code = town_code
        self.town_ship = town_ship

    def validate(self):
        if self.building:
            self.building.validate()
        if self.business_areas:
            for k in self.business_areas:
                if k:
                    k.validate()
        if self.neighborhood:
            self.neighborhood.validate()
        if self.street_number:
            self.street_number.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.building is not None:
            result['building'] = self.building.to_map()
        result['businessAreas'] = []
        if self.business_areas is not None:
            for k in self.business_areas:
                result['businessAreas'].append(k.to_map() if k else None)
        if self.city is not None:
            result['city'] = self.city
        if self.city_code is not None:
            result['cityCode'] = self.city_code
        if self.country is not None:
            result['country'] = self.country
        if self.district is not None:
            result['district'] = self.district
        if self.district_code is not None:
            result['districtCode'] = self.district_code
        if self.formatted_address is not None:
            result['formattedAddress'] = self.formatted_address
        if self.neighborhood is not None:
            result['neighborhood'] = self.neighborhood.to_map()
        if self.province is not None:
            result['province'] = self.province
        if self.street_number is not None:
            result['streetNumber'] = self.street_number.to_map()
        if self.town_code is not None:
            result['townCode'] = self.town_code
        if self.town_ship is not None:
            result['townShip'] = self.town_ship
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('building') is not None:
            temp_model = RgeoCodeResponseBodyDataBuilding()
            self.building = temp_model.from_map(m['building'])
        self.business_areas = []
        if m.get('businessAreas') is not None:
            for k in m.get('businessAreas'):
                temp_model = RgeoCodeResponseBodyDataBusinessAreas()
                self.business_areas.append(temp_model.from_map(k))
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('cityCode') is not None:
            self.city_code = m.get('cityCode')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('districtCode') is not None:
            self.district_code = m.get('districtCode')
        if m.get('formattedAddress') is not None:
            self.formatted_address = m.get('formattedAddress')
        if m.get('neighborhood') is not None:
            temp_model = RgeoCodeResponseBodyDataNeighborhood()
            self.neighborhood = temp_model.from_map(m['neighborhood'])
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('streetNumber') is not None:
            temp_model = RgeoCodeResponseBodyDataStreetNumber()
            self.street_number = temp_model.from_map(m['streetNumber'])
        if m.get('townCode') is not None:
            self.town_code = m.get('townCode')
        if m.get('townShip') is not None:
            self.town_ship = m.get('townShip')
        return self


class RgeoCodeResponseBody(TeaModel):
    def __init__(
        self,
        data: RgeoCodeResponseBodyData = None,
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
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = RgeoCodeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RgeoCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RgeoCodeResponseBody = None,
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
            temp_model = RgeoCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransitIntegratedDirectionRequest(TeaModel):
    def __init__(
        self,
        destination_city: str = None,
        destination_latitude: str = None,
        destination_longitude: str = None,
        origin_city: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
        show_polyline: bool = None,
    ):
        self.destination_city = destination_city
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.origin_city = origin_city
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.show_polyline = show_polyline

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_city is not None:
            result['destinationCity'] = self.destination_city
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.origin_city is not None:
            result['originCity'] = self.origin_city
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        if self.show_polyline is not None:
            result['showPolyline'] = self.show_polyline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destinationCity') is not None:
            self.destination_city = m.get('destinationCity')
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('originCity') is not None:
            self.origin_city = m.get('originCity')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        if m.get('showPolyline') is not None:
            self.show_polyline = m.get('showPolyline')
        return self


class TransitIntegratedDirectionResponseBodyDataCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesArrivalStopExit(TeaModel):
    def __init__(
        self,
        id: str = None,
        location: str = None,
        name: str = None,
    ):
        self.id = id
        self.location = location
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesArrivalStop(TeaModel):
    def __init__(
        self,
        exit: TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesArrivalStopExit = None,
        id: str = None,
        location: str = None,
        name: str = None,
    ):
        self.exit = exit
        self.id = id
        self.location = location
        self.name = name

    def validate(self):
        if self.exit:
            self.exit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exit is not None:
            result['exit'] = self.exit.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exit') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesArrivalStopExit()
            self.exit = temp_model.from_map(m['exit'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesDepartureStopEntrance(TeaModel):
    def __init__(
        self,
        id: str = None,
        location: str = None,
        name: str = None,
    ):
        self.id = id
        self.location = location
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesDepartureStop(TeaModel):
    def __init__(
        self,
        entrance: TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesDepartureStopEntrance = None,
        id: str = None,
        location: str = None,
        name: str = None,
    ):
        self.entrance = entrance
        self.id = id
        self.location = location
        self.name = name

    def validate(self):
        if self.entrance:
            self.entrance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entrance is not None:
            result['entrance'] = self.entrance.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entrance') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesDepartureStopEntrance()
            self.entrance = temp_model.from_map(m['entrance'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesPolyline(TeaModel):
    def __init__(
        self,
        polyline: str = None,
    ):
        self.polyline = polyline

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.polyline is not None:
            result['polyline'] = self.polyline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('polyline') is not None:
            self.polyline = m.get('polyline')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesViaStops(TeaModel):
    def __init__(
        self,
        id: str = None,
        location: str = None,
        name: str = None,
    ):
        self.id = id
        self.location = location
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslines(TeaModel):
    def __init__(
        self,
        arrival_stop: TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesArrivalStop = None,
        bus_time_tips: str = None,
        bustimetag: str = None,
        cost: TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesCost = None,
        departure_stop: TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesDepartureStop = None,
        distance_meter: str = None,
        end_time: str = None,
        id: str = None,
        name: str = None,
        polyline: TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesPolyline = None,
        start_time: str = None,
        type: str = None,
        via_num: str = None,
        via_stops: List[TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesViaStops] = None,
    ):
        self.arrival_stop = arrival_stop
        self.bus_time_tips = bus_time_tips
        self.bustimetag = bustimetag
        self.cost = cost
        self.departure_stop = departure_stop
        self.distance_meter = distance_meter
        self.end_time = end_time
        self.id = id
        self.name = name
        self.polyline = polyline
        self.start_time = start_time
        self.type = type
        self.via_num = via_num
        self.via_stops = via_stops

    def validate(self):
        if self.arrival_stop:
            self.arrival_stop.validate()
        if self.cost:
            self.cost.validate()
        if self.departure_stop:
            self.departure_stop.validate()
        if self.polyline:
            self.polyline.validate()
        if self.via_stops:
            for k in self.via_stops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_stop is not None:
            result['arrivalStop'] = self.arrival_stop.to_map()
        if self.bus_time_tips is not None:
            result['busTimeTips'] = self.bus_time_tips
        if self.bustimetag is not None:
            result['bustimetag'] = self.bustimetag
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.departure_stop is not None:
            result['departureStop'] = self.departure_stop.to_map()
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.polyline is not None:
            result['polyline'] = self.polyline.to_map()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.type is not None:
            result['type'] = self.type
        if self.via_num is not None:
            result['viaNum'] = self.via_num
        result['viaStops'] = []
        if self.via_stops is not None:
            for k in self.via_stops:
                result['viaStops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrivalStop') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesArrivalStop()
            self.arrival_stop = temp_model.from_map(m['arrivalStop'])
        if m.get('busTimeTips') is not None:
            self.bus_time_tips = m.get('busTimeTips')
        if m.get('bustimetag') is not None:
            self.bustimetag = m.get('bustimetag')
        if m.get('cost') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('departureStop') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesDepartureStop()
            self.departure_stop = temp_model.from_map(m['departureStop'])
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('polyline') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesPolyline()
            self.polyline = temp_model.from_map(m['polyline'])
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('viaNum') is not None:
            self.via_num = m.get('viaNum')
        self.via_stops = []
        if m.get('viaStops') is not None:
            for k in m.get('viaStops'):
                temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslinesViaStops()
                self.via_stops.append(temp_model.from_map(k))
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsBus(TeaModel):
    def __init__(
        self,
        buslines: List[TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslines] = None,
        index: str = None,
    ):
        self.buslines = buslines
        self.index = index

    def validate(self):
        if self.buslines:
            for k in self.buslines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['buslines'] = []
        if self.buslines is not None:
            for k in self.buslines:
                result['buslines'].append(k.to_map() if k else None)
        if self.index is not None:
            result['index'] = self.index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.buslines = []
        if m.get('buslines') is not None:
            for k in m.get('buslines'):
                temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsBusBuslines()
                self.buslines.append(temp_model.from_map(k))
        if m.get('index') is not None:
            self.index = m.get('index')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailwayArrivalStop(TeaModel):
    def __init__(
        self,
        adcode: str = None,
        end: str = None,
        id: str = None,
        location: str = None,
        name: str = None,
        time: str = None,
    ):
        self.adcode = adcode
        # end
        self.end = end
        self.id = id
        self.location = location
        self.name = name
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adcode is not None:
            result['adcode'] = self.adcode
        if self.end is not None:
            result['end'] = self.end
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adcode') is not None:
            self.adcode = m.get('adcode')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailwayDepartureStop(TeaModel):
    def __init__(
        self,
        adcode: str = None,
        id: str = None,
        location: str = None,
        name: str = None,
        start: str = None,
        time: str = None,
    ):
        self.adcode = adcode
        self.id = id
        self.location = location
        self.name = name
        self.start = start
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adcode is not None:
            result['adcode'] = self.adcode
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.start is not None:
            result['start'] = self.start
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adcode') is not None:
            self.adcode = m.get('adcode')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailwaySpaces(TeaModel):
    def __init__(
        self,
        code: str = None,
        cost: str = None,
    ):
        self.code = code
        self.cost = cost

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.cost is not None:
            result['cost'] = self.cost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailway(TeaModel):
    def __init__(
        self,
        arrival_stop: TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailwayArrivalStop = None,
        departure_stop: TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailwayDepartureStop = None,
        distance_meter: str = None,
        id: str = None,
        index: str = None,
        name: str = None,
        spaces: List[TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailwaySpaces] = None,
        time: str = None,
        trip: str = None,
        type: str = None,
    ):
        self.arrival_stop = arrival_stop
        self.departure_stop = departure_stop
        self.distance_meter = distance_meter
        self.id = id
        self.index = index
        self.name = name
        self.spaces = spaces
        self.time = time
        self.trip = trip
        self.type = type

    def validate(self):
        if self.arrival_stop:
            self.arrival_stop.validate()
        if self.departure_stop:
            self.departure_stop.validate()
        if self.spaces:
            for k in self.spaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_stop is not None:
            result['arrivalStop'] = self.arrival_stop.to_map()
        if self.departure_stop is not None:
            result['departureStop'] = self.departure_stop.to_map()
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.id is not None:
            result['id'] = self.id
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        result['spaces'] = []
        if self.spaces is not None:
            for k in self.spaces:
                result['spaces'].append(k.to_map() if k else None)
        if self.time is not None:
            result['time'] = self.time
        if self.trip is not None:
            result['trip'] = self.trip
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrivalStop') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailwayArrivalStop()
            self.arrival_stop = temp_model.from_map(m['arrivalStop'])
        if m.get('departureStop') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailwayDepartureStop()
            self.departure_stop = temp_model.from_map(m['departureStop'])
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.spaces = []
        if m.get('spaces') is not None:
            for k in m.get('spaces'):
                temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailwaySpaces()
                self.spaces.append(temp_model.from_map(k))
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('trip') is not None:
            self.trip = m.get('trip')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsTaxiPolyline(TeaModel):
    def __init__(
        self,
        polyline: str = None,
    ):
        self.polyline = polyline

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.polyline is not None:
            result['polyline'] = self.polyline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('polyline') is not None:
            self.polyline = m.get('polyline')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsTaxi(TeaModel):
    def __init__(
        self,
        destination_name: str = None,
        destination_point: str = None,
        distance_meter: str = None,
        drive_time_second: str = None,
        index: str = None,
        origin_name: str = None,
        origin_point: str = None,
        polyline: TransitIntegratedDirectionResponseBodyDataPathsSegmentsTaxiPolyline = None,
        price: str = None,
    ):
        self.destination_name = destination_name
        self.destination_point = destination_point
        self.distance_meter = distance_meter
        self.drive_time_second = drive_time_second
        self.index = index
        self.origin_name = origin_name
        self.origin_point = origin_point
        self.polyline = polyline
        self.price = price

    def validate(self):
        if self.polyline:
            self.polyline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_name is not None:
            result['destinationName'] = self.destination_name
        if self.destination_point is not None:
            result['destinationPoint'] = self.destination_point
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.drive_time_second is not None:
            result['driveTimeSecond'] = self.drive_time_second
        if self.index is not None:
            result['index'] = self.index
        if self.origin_name is not None:
            result['originName'] = self.origin_name
        if self.origin_point is not None:
            result['originPoint'] = self.origin_point
        if self.polyline is not None:
            result['polyline'] = self.polyline.to_map()
        if self.price is not None:
            result['price'] = self.price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destinationName') is not None:
            self.destination_name = m.get('destinationName')
        if m.get('destinationPoint') is not None:
            self.destination_point = m.get('destinationPoint')
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('driveTimeSecond') is not None:
            self.drive_time_second = m.get('driveTimeSecond')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('originName') is not None:
            self.origin_name = m.get('originName')
        if m.get('originPoint') is not None:
            self.origin_point = m.get('originPoint')
        if m.get('polyline') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsTaxiPolyline()
            self.polyline = temp_model.from_map(m['polyline'])
        if m.get('price') is not None:
            self.price = m.get('price')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingStepsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingStepsPolyline(TeaModel):
    def __init__(
        self,
        polyline: str = None,
    ):
        self.polyline = polyline

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.polyline is not None:
            result['polyline'] = self.polyline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('polyline') is not None:
            self.polyline = m.get('polyline')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingSteps(TeaModel):
    def __init__(
        self,
        cost: TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingStepsCost = None,
        instruction: str = None,
        orientation: str = None,
        polyline: TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingStepsPolyline = None,
        road_name: str = None,
        step_distance_meter: str = None,
    ):
        self.cost = cost
        self.instruction = instruction
        self.orientation = orientation
        self.polyline = polyline
        self.road_name = road_name
        self.step_distance_meter = step_distance_meter

    def validate(self):
        if self.cost:
            self.cost.validate()
        if self.polyline:
            self.polyline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.instruction is not None:
            result['instruction'] = self.instruction
        if self.orientation is not None:
            result['orientation'] = self.orientation
        if self.polyline is not None:
            result['polyline'] = self.polyline.to_map()
        if self.road_name is not None:
            result['roadName'] = self.road_name
        if self.step_distance_meter is not None:
            result['stepDistanceMeter'] = self.step_distance_meter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingStepsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')
        if m.get('orientation') is not None:
            self.orientation = m.get('orientation')
        if m.get('polyline') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingStepsPolyline()
            self.polyline = temp_model.from_map(m['polyline'])
        if m.get('roadName') is not None:
            self.road_name = m.get('roadName')
        if m.get('stepDistanceMeter') is not None:
            self.step_distance_meter = m.get('stepDistanceMeter')
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalking(TeaModel):
    def __init__(
        self,
        cost: TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingCost = None,
        destination: str = None,
        distance_meter: str = None,
        index: str = None,
        origin: str = None,
        steps: List[TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingSteps] = None,
    ):
        self.cost = cost
        self.destination = destination
        self.distance_meter = distance_meter
        self.index = index
        self.origin = origin
        self.steps = steps

    def validate(self):
        if self.cost:
            self.cost.validate()
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.destination is not None:
            result['destination'] = self.destination
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.index is not None:
            result['index'] = self.index
        if self.origin is not None:
            result['origin'] = self.origin
        result['steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['steps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('destination') is not None:
            self.destination = m.get('destination')
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('origin') is not None:
            self.origin = m.get('origin')
        self.steps = []
        if m.get('steps') is not None:
            for k in m.get('steps'):
                temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalkingSteps()
                self.steps.append(temp_model.from_map(k))
        return self


class TransitIntegratedDirectionResponseBodyDataPathsSegments(TeaModel):
    def __init__(
        self,
        bus: TransitIntegratedDirectionResponseBodyDataPathsSegmentsBus = None,
        railway: TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailway = None,
        taxi: TransitIntegratedDirectionResponseBodyDataPathsSegmentsTaxi = None,
        walking: TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalking = None,
    ):
        self.bus = bus
        self.railway = railway
        self.taxi = taxi
        self.walking = walking

    def validate(self):
        if self.bus:
            self.bus.validate()
        if self.railway:
            self.railway.validate()
        if self.taxi:
            self.taxi.validate()
        if self.walking:
            self.walking.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bus is not None:
            result['bus'] = self.bus.to_map()
        if self.railway is not None:
            result['railway'] = self.railway.to_map()
        if self.taxi is not None:
            result['taxi'] = self.taxi.to_map()
        if self.walking is not None:
            result['walking'] = self.walking.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bus') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsBus()
            self.bus = temp_model.from_map(m['bus'])
        if m.get('railway') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsRailway()
            self.railway = temp_model.from_map(m['railway'])
        if m.get('taxi') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsTaxi()
            self.taxi = temp_model.from_map(m['taxi'])
        if m.get('walking') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegmentsWalking()
            self.walking = temp_model.from_map(m['walking'])
        return self


class TransitIntegratedDirectionResponseBodyDataPaths(TeaModel):
    def __init__(
        self,
        cost: TransitIntegratedDirectionResponseBodyDataPathsCost = None,
        distance_meter: str = None,
        nightflag: str = None,
        segments: List[TransitIntegratedDirectionResponseBodyDataPathsSegments] = None,
        walking_distance_meter: str = None,
    ):
        self.cost = cost
        self.distance_meter = distance_meter
        self.nightflag = nightflag
        self.segments = segments
        self.walking_distance_meter = walking_distance_meter

    def validate(self):
        if self.cost:
            self.cost.validate()
        if self.segments:
            for k in self.segments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.nightflag is not None:
            result['nightflag'] = self.nightflag
        result['segments'] = []
        if self.segments is not None:
            for k in self.segments:
                result['segments'].append(k.to_map() if k else None)
        if self.walking_distance_meter is not None:
            result['walkingDistanceMeter'] = self.walking_distance_meter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataPathsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('nightflag') is not None:
            self.nightflag = m.get('nightflag')
        self.segments = []
        if m.get('segments') is not None:
            for k in m.get('segments'):
                temp_model = TransitIntegratedDirectionResponseBodyDataPathsSegments()
                self.segments.append(temp_model.from_map(k))
        if m.get('walkingDistanceMeter') is not None:
            self.walking_distance_meter = m.get('walkingDistanceMeter')
        return self


class TransitIntegratedDirectionResponseBodyData(TeaModel):
    def __init__(
        self,
        cost: TransitIntegratedDirectionResponseBodyDataCost = None,
        count: str = None,
        destination_latitude: str = None,
        destination_longitude: str = None,
        distance_meter: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
        paths: List[TransitIntegratedDirectionResponseBodyDataPaths] = None,
    ):
        self.cost = cost
        self.count = count
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.distance_meter = distance_meter
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.paths = paths

    def validate(self):
        if self.cost:
            self.cost.validate()
        if self.paths:
            for k in self.paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.count is not None:
            result['count'] = self.count
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        result['paths'] = []
        if self.paths is not None:
            for k in self.paths:
                result['paths'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyDataCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        self.paths = []
        if m.get('paths') is not None:
            for k in m.get('paths'):
                temp_model = TransitIntegratedDirectionResponseBodyDataPaths()
                self.paths.append(temp_model.from_map(k))
        return self


class TransitIntegratedDirectionResponseBody(TeaModel):
    def __init__(
        self,
        data: TransitIntegratedDirectionResponseBodyData = None,
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
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = TransitIntegratedDirectionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class TransitIntegratedDirectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransitIntegratedDirectionResponseBody = None,
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
            temp_model = TransitIntegratedDirectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WalkingDirectionNovaRequest(TeaModel):
    def __init__(
        self,
        destination_latitude: str = None,
        destination_longitude: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
        show_polyline: bool = None,
    ):
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.show_polyline = show_polyline

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        if self.show_polyline is not None:
            result['showPolyline'] = self.show_polyline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        if m.get('showPolyline') is not None:
            self.show_polyline = m.get('showPolyline')
        return self


class WalkingDirectionNovaResponseBodyDataPathsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class WalkingDirectionNovaResponseBodyDataPathsStepsCost(TeaModel):
    def __init__(
        self,
        duration_second: str = None,
        taxi_fee: str = None,
        toll_distance_meter: str = None,
        toll_roads: str = None,
        tolls: str = None,
        traffic_lights: str = None,
        transit_fee: str = None,
    ):
        self.duration_second = duration_second
        self.taxi_fee = taxi_fee
        self.toll_distance_meter = toll_distance_meter
        self.toll_roads = toll_roads
        self.tolls = tolls
        self.traffic_lights = traffic_lights
        self.transit_fee = transit_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.taxi_fee is not None:
            result['taxiFee'] = self.taxi_fee
        if self.toll_distance_meter is not None:
            result['tollDistanceMeter'] = self.toll_distance_meter
        if self.toll_roads is not None:
            result['tollRoads'] = self.toll_roads
        if self.tolls is not None:
            result['tolls'] = self.tolls
        if self.traffic_lights is not None:
            result['trafficLights'] = self.traffic_lights
        if self.transit_fee is not None:
            result['transitFee'] = self.transit_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('taxiFee') is not None:
            self.taxi_fee = m.get('taxiFee')
        if m.get('tollDistanceMeter') is not None:
            self.toll_distance_meter = m.get('tollDistanceMeter')
        if m.get('tollRoads') is not None:
            self.toll_roads = m.get('tollRoads')
        if m.get('tolls') is not None:
            self.tolls = m.get('tolls')
        if m.get('trafficLights') is not None:
            self.traffic_lights = m.get('trafficLights')
        if m.get('transitFee') is not None:
            self.transit_fee = m.get('transitFee')
        return self


class WalkingDirectionNovaResponseBodyDataPathsSteps(TeaModel):
    def __init__(
        self,
        cost: WalkingDirectionNovaResponseBodyDataPathsStepsCost = None,
        instruction: str = None,
        orientation: str = None,
        polyline: str = None,
        road_name: str = None,
        step_distance_meter: str = None,
    ):
        self.cost = cost
        self.instruction = instruction
        self.orientation = orientation
        self.polyline = polyline
        self.road_name = road_name
        self.step_distance_meter = step_distance_meter

    def validate(self):
        if self.cost:
            self.cost.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.instruction is not None:
            result['instruction'] = self.instruction
        if self.orientation is not None:
            result['orientation'] = self.orientation
        if self.polyline is not None:
            result['polyline'] = self.polyline
        if self.road_name is not None:
            result['roadName'] = self.road_name
        if self.step_distance_meter is not None:
            result['stepDistanceMeter'] = self.step_distance_meter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = WalkingDirectionNovaResponseBodyDataPathsStepsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')
        if m.get('orientation') is not None:
            self.orientation = m.get('orientation')
        if m.get('polyline') is not None:
            self.polyline = m.get('polyline')
        if m.get('roadName') is not None:
            self.road_name = m.get('roadName')
        if m.get('stepDistanceMeter') is not None:
            self.step_distance_meter = m.get('stepDistanceMeter')
        return self


class WalkingDirectionNovaResponseBodyDataPaths(TeaModel):
    def __init__(
        self,
        cost: WalkingDirectionNovaResponseBodyDataPathsCost = None,
        distance_meter: str = None,
        duration_second: str = None,
        restriction: str = None,
        steps: List[WalkingDirectionNovaResponseBodyDataPathsSteps] = None,
    ):
        self.cost = cost
        self.distance_meter = distance_meter
        self.duration_second = duration_second
        self.restriction = restriction
        self.steps = steps

    def validate(self):
        if self.cost:
            self.cost.validate()
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost.to_map()
        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter
        if self.duration_second is not None:
            result['durationSecond'] = self.duration_second
        if self.restriction is not None:
            result['restriction'] = self.restriction
        result['steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['steps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            temp_model = WalkingDirectionNovaResponseBodyDataPathsCost()
            self.cost = temp_model.from_map(m['cost'])
        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')
        if m.get('durationSecond') is not None:
            self.duration_second = m.get('durationSecond')
        if m.get('restriction') is not None:
            self.restriction = m.get('restriction')
        self.steps = []
        if m.get('steps') is not None:
            for k in m.get('steps'):
                temp_model = WalkingDirectionNovaResponseBodyDataPathsSteps()
                self.steps.append(temp_model.from_map(k))
        return self


class WalkingDirectionNovaResponseBodyData(TeaModel):
    def __init__(
        self,
        count: str = None,
        destination_latitude: str = None,
        destination_longitude: str = None,
        origin_latitude: str = None,
        origin_longitude: str = None,
        paths: List[WalkingDirectionNovaResponseBodyDataPaths] = None,
        taxi_cost: str = None,
    ):
        self.count = count
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.paths = paths
        self.taxi_cost = taxi_cost

    def validate(self):
        if self.paths:
            for k in self.paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.destination_latitude is not None:
            result['destinationLatitude'] = self.destination_latitude
        if self.destination_longitude is not None:
            result['destinationLongitude'] = self.destination_longitude
        if self.origin_latitude is not None:
            result['originLatitude'] = self.origin_latitude
        if self.origin_longitude is not None:
            result['originLongitude'] = self.origin_longitude
        result['paths'] = []
        if self.paths is not None:
            for k in self.paths:
                result['paths'].append(k.to_map() if k else None)
        if self.taxi_cost is not None:
            result['taxiCost'] = self.taxi_cost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('destinationLatitude') is not None:
            self.destination_latitude = m.get('destinationLatitude')
        if m.get('destinationLongitude') is not None:
            self.destination_longitude = m.get('destinationLongitude')
        if m.get('originLatitude') is not None:
            self.origin_latitude = m.get('originLatitude')
        if m.get('originLongitude') is not None:
            self.origin_longitude = m.get('originLongitude')
        self.paths = []
        if m.get('paths') is not None:
            for k in m.get('paths'):
                temp_model = WalkingDirectionNovaResponseBodyDataPaths()
                self.paths.append(temp_model.from_map(k))
        if m.get('taxiCost') is not None:
            self.taxi_cost = m.get('taxiCost')
        return self


class WalkingDirectionNovaResponseBody(TeaModel):
    def __init__(
        self,
        data: WalkingDirectionNovaResponseBodyData = None,
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
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = WalkingDirectionNovaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class WalkingDirectionNovaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: WalkingDirectionNovaResponseBody = None,
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
            temp_model = WalkingDirectionNovaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


