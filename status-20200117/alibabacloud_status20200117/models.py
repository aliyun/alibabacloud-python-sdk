# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ListEventInProgressRequest(TeaModel):
    def __init__(
        self,
        region_ids: List[str] = None,
    ):
        self.region_ids = region_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        return self


class ListEventInProgressShrinkRequest(TeaModel):
    def __init__(
        self,
        region_ids_shrink: str = None,
    ):
        self.region_ids_shrink = region_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        return self


class ListEventInProgressResponseBodyDataEventUpdates(TeaModel):
    def __init__(
        self,
        content: str = None,
        publish_time: int = None,
    ):
        self.content = content
        self.publish_time = publish_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        return self


class ListEventInProgressResponseBodyDataImpactsProduct(TeaModel):
    def __init__(
        self,
        product_id: str = None,
        product_name: str = None,
    ):
        self.product_id = product_id
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class ListEventInProgressResponseBodyDataImpactsRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
    ):
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class ListEventInProgressResponseBodyDataImpacts(TeaModel):
    def __init__(
        self,
        product: ListEventInProgressResponseBodyDataImpactsProduct = None,
        recovery_time: int = None,
        region: ListEventInProgressResponseBodyDataImpactsRegion = None,
        start_time: int = None,
    ):
        self.product = product
        self.recovery_time = recovery_time
        self.region = region
        self.start_time = start_time

    def validate(self):
        if self.product:
            self.product.validate()
        if self.region:
            self.region.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product.to_map()
        if self.recovery_time is not None:
            result['RecoveryTime'] = self.recovery_time
        if self.region is not None:
            result['Region'] = self.region.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            temp_model = ListEventInProgressResponseBodyDataImpactsProduct()
            self.product = temp_model.from_map(m['Product'])
        if m.get('RecoveryTime') is not None:
            self.recovery_time = m.get('RecoveryTime')
        if m.get('Region') is not None:
            temp_model = ListEventInProgressResponseBodyDataImpactsRegion()
            self.region = temp_model.from_map(m['Region'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListEventInProgressResponseBodyData(TeaModel):
    def __init__(
        self,
        event_updates: List[ListEventInProgressResponseBodyDataEventUpdates] = None,
        id: int = None,
        impacts: List[ListEventInProgressResponseBodyDataImpacts] = None,
        start_time: int = None,
        title: str = None,
    ):
        self.event_updates = event_updates
        self.id = id
        self.impacts = impacts
        self.start_time = start_time
        self.title = title

    def validate(self):
        if self.event_updates:
            for k in self.event_updates:
                if k:
                    k.validate()
        if self.impacts:
            for k in self.impacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventUpdates'] = []
        if self.event_updates is not None:
            for k in self.event_updates:
                result['EventUpdates'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        result['Impacts'] = []
        if self.impacts is not None:
            for k in self.impacts:
                result['Impacts'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_updates = []
        if m.get('EventUpdates') is not None:
            for k in m.get('EventUpdates'):
                temp_model = ListEventInProgressResponseBodyDataEventUpdates()
                self.event_updates.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.impacts = []
        if m.get('Impacts') is not None:
            for k in m.get('Impacts'):
                temp_model = ListEventInProgressResponseBodyDataImpacts()
                self.impacts.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListEventInProgressResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListEventInProgressResponseBodyData] = None,
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEventInProgressResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEventInProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventInProgressResponseBody = None,
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
            temp_model = ListEventInProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


