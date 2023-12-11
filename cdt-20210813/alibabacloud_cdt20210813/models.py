# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCdtCbServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        request_id: str = None,
    ):
        self.enabled = enabled
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCdtCbServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCdtCbServiceStatusResponseBody = None,
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
            temp_model = GetCdtCbServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCdtInternetServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        request_id: str = None,
    ):
        self.enabled = enabled
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCdtInternetServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCdtInternetServiceStatusResponseBody = None,
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
            temp_model = GetCdtInternetServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCdtServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        request_id: str = None,
    ):
        self.enabled = enabled
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCdtServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCdtServiceStatusResponseBody = None,
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
            temp_model = GetCdtServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCdtCrossBordTrafficRequest(TeaModel):
    def __init__(
        self,
        business_region_id: str = None,
    ):
        self.business_region_id = business_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')
        return self


class ListCdtCrossBordTrafficResponseBodyTrafficDetailsProductTrafficDetails(TeaModel):
    def __init__(
        self,
        product: str = None,
        traffic: int = None,
    ):
        self.product = product
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class ListCdtCrossBordTrafficResponseBodyTrafficDetails(TeaModel):
    def __init__(
        self,
        business_region_id: str = None,
        product_traffic_details: List[ListCdtCrossBordTrafficResponseBodyTrafficDetailsProductTrafficDetails] = None,
        traffic: int = None,
    ):
        self.business_region_id = business_region_id
        self.product_traffic_details = product_traffic_details
        self.traffic = traffic

    def validate(self):
        if self.product_traffic_details:
            for k in self.product_traffic_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id
        result['ProductTrafficDetails'] = []
        if self.product_traffic_details is not None:
            for k in self.product_traffic_details:
                result['ProductTrafficDetails'].append(k.to_map() if k else None)
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')
        self.product_traffic_details = []
        if m.get('ProductTrafficDetails') is not None:
            for k in m.get('ProductTrafficDetails'):
                temp_model = ListCdtCrossBordTrafficResponseBodyTrafficDetailsProductTrafficDetails()
                self.product_traffic_details.append(temp_model.from_map(k))
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class ListCdtCrossBordTrafficResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_details: List[ListCdtCrossBordTrafficResponseBodyTrafficDetails] = None,
    ):
        self.request_id = request_id
        self.traffic_details = traffic_details

    def validate(self):
        if self.traffic_details:
            for k in self.traffic_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TrafficDetails'] = []
        if self.traffic_details is not None:
            for k in self.traffic_details:
                result['TrafficDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.traffic_details = []
        if m.get('TrafficDetails') is not None:
            for k in m.get('TrafficDetails'):
                temp_model = ListCdtCrossBordTrafficResponseBodyTrafficDetails()
                self.traffic_details.append(temp_model.from_map(k))
        return self


class ListCdtCrossBordTrafficResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCdtCrossBordTrafficResponseBody = None,
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
            temp_model = ListCdtCrossBordTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCdtInternetTrafficRequest(TeaModel):
    def __init__(
        self,
        business_region_id: str = None,
    ):
        self.business_region_id = business_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')
        return self


class ListCdtInternetTrafficResponseBodyTrafficDetailsProductTrafficDetails(TeaModel):
    def __init__(
        self,
        product: str = None,
        traffic: int = None,
    ):
        self.product = product
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class ListCdtInternetTrafficResponseBodyTrafficDetailsTrafficTierDetails(TeaModel):
    def __init__(
        self,
        highest_traffic: int = None,
        lowest_traffic: int = None,
        tier: int = None,
        traffic: int = None,
    ):
        self.highest_traffic = highest_traffic
        self.lowest_traffic = lowest_traffic
        self.tier = tier
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.highest_traffic is not None:
            result['HighestTraffic'] = self.highest_traffic
        if self.lowest_traffic is not None:
            result['LowestTraffic'] = self.lowest_traffic
        if self.tier is not None:
            result['Tier'] = self.tier
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HighestTraffic') is not None:
            self.highest_traffic = m.get('HighestTraffic')
        if m.get('LowestTraffic') is not None:
            self.lowest_traffic = m.get('LowestTraffic')
        if m.get('Tier') is not None:
            self.tier = m.get('Tier')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class ListCdtInternetTrafficResponseBodyTrafficDetails(TeaModel):
    def __init__(
        self,
        business_region_id: str = None,
        isptype: str = None,
        product_traffic_details: List[ListCdtInternetTrafficResponseBodyTrafficDetailsProductTrafficDetails] = None,
        traffic: int = None,
        traffic_tier_details: List[ListCdtInternetTrafficResponseBodyTrafficDetailsTrafficTierDetails] = None,
    ):
        self.business_region_id = business_region_id
        self.isptype = isptype
        self.product_traffic_details = product_traffic_details
        self.traffic = traffic
        self.traffic_tier_details = traffic_tier_details

    def validate(self):
        if self.product_traffic_details:
            for k in self.product_traffic_details:
                if k:
                    k.validate()
        if self.traffic_tier_details:
            for k in self.traffic_tier_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id
        if self.isptype is not None:
            result['ISPType'] = self.isptype
        result['ProductTrafficDetails'] = []
        if self.product_traffic_details is not None:
            for k in self.product_traffic_details:
                result['ProductTrafficDetails'].append(k.to_map() if k else None)
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        result['TrafficTierDetails'] = []
        if self.traffic_tier_details is not None:
            for k in self.traffic_tier_details:
                result['TrafficTierDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')
        if m.get('ISPType') is not None:
            self.isptype = m.get('ISPType')
        self.product_traffic_details = []
        if m.get('ProductTrafficDetails') is not None:
            for k in m.get('ProductTrafficDetails'):
                temp_model = ListCdtInternetTrafficResponseBodyTrafficDetailsProductTrafficDetails()
                self.product_traffic_details.append(temp_model.from_map(k))
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        self.traffic_tier_details = []
        if m.get('TrafficTierDetails') is not None:
            for k in m.get('TrafficTierDetails'):
                temp_model = ListCdtInternetTrafficResponseBodyTrafficDetailsTrafficTierDetails()
                self.traffic_tier_details.append(temp_model.from_map(k))
        return self


class ListCdtInternetTrafficResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_details: List[ListCdtInternetTrafficResponseBodyTrafficDetails] = None,
    ):
        self.request_id = request_id
        self.traffic_details = traffic_details

    def validate(self):
        if self.traffic_details:
            for k in self.traffic_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TrafficDetails'] = []
        if self.traffic_details is not None:
            for k in self.traffic_details:
                result['TrafficDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.traffic_details = []
        if m.get('TrafficDetails') is not None:
            for k in m.get('TrafficDetails'):
                temp_model = ListCdtInternetTrafficResponseBodyTrafficDetails()
                self.traffic_details.append(temp_model.from_map(k))
        return self


class ListCdtInternetTrafficResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCdtInternetTrafficResponseBody = None,
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
            temp_model = ListCdtInternetTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCdtProductsRequest(TeaModel):
    def __init__(
        self,
        business_region_id: str = None,
        product: str = None,
    ):
        self.business_region_id = business_region_id
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class ListCdtProductsResponseBodyCdtProducts(TeaModel):
    def __init__(
        self,
        billing_type: str = None,
        business_region_id: str = None,
        cdt_type: str = None,
        effective_time: int = None,
        expire_time: int = None,
        product: str = None,
        switched_to_cdt: bool = None,
    ):
        self.billing_type = billing_type
        self.business_region_id = business_region_id
        self.cdt_type = cdt_type
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.product = product
        self.switched_to_cdt = switched_to_cdt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id
        if self.cdt_type is not None:
            result['CdtType'] = self.cdt_type
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.product is not None:
            result['Product'] = self.product
        if self.switched_to_cdt is not None:
            result['SwitchedToCdt'] = self.switched_to_cdt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')
        if m.get('CdtType') is not None:
            self.cdt_type = m.get('CdtType')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('SwitchedToCdt') is not None:
            self.switched_to_cdt = m.get('SwitchedToCdt')
        return self


class ListCdtProductsResponseBody(TeaModel):
    def __init__(
        self,
        cdt_products: List[ListCdtProductsResponseBodyCdtProducts] = None,
        request_id: str = None,
    ):
        self.cdt_products = cdt_products
        self.request_id = request_id

    def validate(self):
        if self.cdt_products:
            for k in self.cdt_products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CdtProducts'] = []
        if self.cdt_products is not None:
            for k in self.cdt_products:
                result['CdtProducts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cdt_products = []
        if m.get('CdtProducts') is not None:
            for k in m.get('CdtProducts'):
                temp_model = ListCdtProductsResponseBodyCdtProducts()
                self.cdt_products.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCdtProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCdtProductsResponseBody = None,
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
            temp_model = ListCdtProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCdtTrafficTiersRequest(TeaModel):
    def __init__(
        self,
        business_region_id: str = None,
    ):
        self.business_region_id = business_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')
        return self


class ListCdtTrafficTiersResponseBodyTrafficTiers(TeaModel):
    def __init__(
        self,
        highest_traffic: int = None,
        lowest_traffic: int = None,
        tier: int = None,
    ):
        self.highest_traffic = highest_traffic
        self.lowest_traffic = lowest_traffic
        self.tier = tier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.highest_traffic is not None:
            result['HighestTraffic'] = self.highest_traffic
        if self.lowest_traffic is not None:
            result['LowestTraffic'] = self.lowest_traffic
        if self.tier is not None:
            result['Tier'] = self.tier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HighestTraffic') is not None:
            self.highest_traffic = m.get('HighestTraffic')
        if m.get('LowestTraffic') is not None:
            self.lowest_traffic = m.get('LowestTraffic')
        if m.get('Tier') is not None:
            self.tier = m.get('Tier')
        return self


class ListCdtTrafficTiersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_tiers: List[ListCdtTrafficTiersResponseBodyTrafficTiers] = None,
    ):
        self.request_id = request_id
        self.traffic_tiers = traffic_tiers

    def validate(self):
        if self.traffic_tiers:
            for k in self.traffic_tiers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TrafficTiers'] = []
        if self.traffic_tiers is not None:
            for k in self.traffic_tiers:
                result['TrafficTiers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.traffic_tiers = []
        if m.get('TrafficTiers') is not None:
            for k in m.get('TrafficTiers'):
                temp_model = ListCdtTrafficTiersResponseBodyTrafficTiers()
                self.traffic_tiers.append(temp_model.from_map(k))
        return self


class ListCdtTrafficTiersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCdtTrafficTiersResponseBody = None,
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
            temp_model = ListCdtTrafficTiersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSwitchedCdtProductsRequest(TeaModel):
    def __init__(
        self,
        business_region_id: str = None,
        product: str = None,
    ):
        self.business_region_id = business_region_id
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class ListSwitchedCdtProductsResponseBodyCdtProducts(TeaModel):
    def __init__(
        self,
        billing_type: str = None,
        business_region_id: str = None,
        cdt_type: str = None,
        effective_time: int = None,
        expire_time: int = None,
        product: str = None,
    ):
        self.billing_type = billing_type
        self.business_region_id = business_region_id
        self.cdt_type = cdt_type
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id
        if self.cdt_type is not None:
            result['CdtType'] = self.cdt_type
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')
        if m.get('CdtType') is not None:
            self.cdt_type = m.get('CdtType')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class ListSwitchedCdtProductsResponseBody(TeaModel):
    def __init__(
        self,
        cdt_products: List[ListSwitchedCdtProductsResponseBodyCdtProducts] = None,
        request_id: str = None,
    ):
        self.cdt_products = cdt_products
        self.request_id = request_id

    def validate(self):
        if self.cdt_products:
            for k in self.cdt_products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CdtProducts'] = []
        if self.cdt_products is not None:
            for k in self.cdt_products:
                result['CdtProducts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cdt_products = []
        if m.get('CdtProducts') is not None:
            for k in m.get('CdtProducts'):
                temp_model = ListSwitchedCdtProductsResponseBodyCdtProducts()
                self.cdt_products.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSwitchedCdtProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSwitchedCdtProductsResponseBody = None,
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
            temp_model = ListSwitchedCdtProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenCdtCbServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenCdtCbServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenCdtCbServiceResponseBody = None,
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
            temp_model = OpenCdtCbServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenCdtInternetServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenCdtInternetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenCdtInternetServiceResponseBody = None,
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
            temp_model = OpenCdtInternetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenCdtServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenCdtServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenCdtServiceResponseBody = None,
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
            temp_model = OpenCdtServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchToCdtRequest(TeaModel):
    def __init__(
        self,
        billing_type: str = None,
        business_region_id: str = None,
        product: str = None,
    ):
        self.billing_type = billing_type
        self.business_region_id = business_region_id
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class SwitchToCdtResponseBody(TeaModel):
    def __init__(
        self,
        effective_time: int = None,
        request_id: str = None,
    ):
        self.effective_time = effective_time
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchToCdtResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchToCdtResponseBody = None,
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
            temp_model = SwitchToCdtResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


