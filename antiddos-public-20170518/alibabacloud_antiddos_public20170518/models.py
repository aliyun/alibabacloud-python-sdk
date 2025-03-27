# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DescribeBgpPackByIpRequest(TeaModel):
    def __init__(
        self,
        ddos_region_id: str = None,
        ip: str = None,
    ):
        # The region ID of the asset to query.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The IP address of the asset to query.
        # 
        # >  You can call the [DescribeInstanceIpAddress](https://help.aliyun.com/document_detail/472620.html) operation to query the IDs of Elastic Compute Service (ECS) instances, Server Load Balancer (SLB) instances, and elastic IP addresses (EIPs) within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeBgpPackByIpResponseBodyDdosbgpInfo(TeaModel):
    def __init__(
        self,
        base_threshold: int = None,
        ddosbgp_instance_id: str = None,
        elastic_threshold: int = None,
        expire_time: int = None,
        ip: str = None,
    ):
        # The basic protection threshold of the instance. Unit: Gbit/s.
        self.base_threshold = base_threshold
        # The ID of the instance.
        self.ddosbgp_instance_id = ddosbgp_instance_id
        # The burstable protection threshold of the instance. Unit: Gbit/s.
        self.elastic_threshold = elastic_threshold
        # The expiration time of the instance. The value is a UNIX timestamp. Unit: milliseconds.
        self.expire_time = expire_time
        # The IP address of the asset.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_threshold is not None:
            result['BaseThreshold'] = self.base_threshold
        if self.ddosbgp_instance_id is not None:
            result['DdosbgpInstanceId'] = self.ddosbgp_instance_id
        if self.elastic_threshold is not None:
            result['ElasticThreshold'] = self.elastic_threshold
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseThreshold') is not None:
            self.base_threshold = m.get('BaseThreshold')
        if m.get('DdosbgpInstanceId') is not None:
            self.ddosbgp_instance_id = m.get('DdosbgpInstanceId')
        if m.get('ElasticThreshold') is not None:
            self.elastic_threshold = m.get('ElasticThreshold')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeBgpPackByIpResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ddosbgp_info: DescribeBgpPackByIpResponseBodyDdosbgpInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code of the request.
        # 
        # For more information about status codes, see [Common parameters](https://help.aliyun.com/document_detail/118841.html).
        self.code = code
        # The configurations of the instance that is associated with the asset.
        self.ddosbgp_info = ddosbgp_info
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success

    def validate(self):
        if self.ddosbgp_info:
            self.ddosbgp_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ddosbgp_info is not None:
            result['DdosbgpInfo'] = self.ddosbgp_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DdosbgpInfo') is not None:
            temp_model = DescribeBgpPackByIpResponseBodyDdosbgpInfo()
            self.ddosbgp_info = temp_model.from_map(m['DdosbgpInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBgpPackByIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBgpPackByIpResponseBody = None,
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
            temp_model = DescribeBgpPackByIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCapRequest(TeaModel):
    def __init__(
        self,
        beg_time: int = None,
        ddos_region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_ip: str = None,
    ):
        # The start time of the DDoS attack event. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > You can call the [DescribeDdosEventList](https://help.aliyun.com/document_detail/354236.html) operation to query the start time of each DDoS attack event that occurred on an asset.
        # 
        # This parameter is required.
        self.beg_time = beg_time
        # The region ID of the asset that is under DDoS attacks. The asset is assigned a public IP address.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The ID of the asset that is under DDoS attacks.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/354191.html) operation to query the IDs of ECS instances, SLB instances, and EIPs within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the asset that is under DDoS attacks. The asset is assigned a public IP address. Valid values:
        # 
        # *   **ecs**: an Elastic Compute Service (ECS) instance.
        # *   **slb**: a Server Load Balancer (SLB) instance.
        # *   **eip**: an elastic IP address (EIP).
        # *   **ipv6**: an IPv6 gateway.
        # *   **swas**: a simple application server.
        # *   **waf**: a Web Application Firewall (WAF) instance of the Exclusive edition.
        # *   **ga_basic**: a Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The public IP address of the asset that is under DDoS attacks.
        self.internet_ip = internet_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beg_time is not None:
            result['BegTime'] = self.beg_time
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BegTime') is not None:
            self.beg_time = m.get('BegTime')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        return self


class DescribeCapResponseBodyCapUrl(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        # The download link to the traffic data.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeCapResponseBody(TeaModel):
    def __init__(
        self,
        cap_url: DescribeCapResponseBodyCapUrl = None,
        request_id: str = None,
    ):
        # The download link to the traffic data that is captured when a DDoS attack event occurs.
        self.cap_url = cap_url
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.cap_url:
            self.cap_url.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cap_url is not None:
            result['CapUrl'] = self.cap_url.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapUrl') is not None:
            temp_model = DescribeCapResponseBodyCapUrl()
            self.cap_url = temp_model.from_map(m['CapUrl'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCapResponseBody = None,
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
            temp_model = DescribeCapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosCountRequest(TeaModel):
    def __init__(
        self,
        ddos_region_id: str = None,
        instance_type: str = None,
    ):
        # The region ID of the asset to query.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The type of the asset to query. Valid values:
        # 
        # *   **ecs**: Elastic Compute Service (ECS) instances.
        # *   **slb**: Server Load Balancer (SLB) instances.
        # *   **eip**: elastic IP addresses (EIPs).
        # *   **ipv6**: IPv6 gateways.
        # *   **swas**: simple application servers.
        # *   **waf**: Web Application Firewall (WAF) instances of the Exclusive edition.
        # *   **ga_basic**: Global Accelerator (GA) instances.
        # 
        # This parameter is required.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeDdosCountResponseBodyDdosCount(TeaModel):
    def __init__(
        self,
        blackhole_count: int = None,
        defense_count: int = None,
        instacen_count: int = None,
    ):
        # The number of assets for which blackhole filtering is triggered.
        self.blackhole_count = blackhole_count
        # The number of assets for which traffic scrubbing is triggered.
        self.defense_count = defense_count
        # The total number of assets.
        self.instacen_count = instacen_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackhole_count is not None:
            result['BlackholeCount'] = self.blackhole_count
        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count
        if self.instacen_count is not None:
            result['InstacenCount'] = self.instacen_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackholeCount') is not None:
            self.blackhole_count = m.get('BlackholeCount')
        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')
        if m.get('InstacenCount') is not None:
            self.instacen_count = m.get('InstacenCount')
        return self


class DescribeDdosCountResponseBody(TeaModel):
    def __init__(
        self,
        ddos_count: DescribeDdosCountResponseBodyDdosCount = None,
        request_id: str = None,
    ):
        # The number of assets that are under DDoS attacks.
        self.ddos_count = ddos_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ddos_count:
            self.ddos_count.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_count is not None:
            result['DdosCount'] = self.ddos_count.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosCount') is not None:
            temp_model = DescribeDdosCountResponseBodyDdosCount()
            self.ddos_count = temp_model.from_map(m['DdosCount'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDdosCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDdosCountResponseBody = None,
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
            temp_model = DescribeDdosCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosCreditRequest(TeaModel):
    def __init__(
        self,
        ddos_region_id: str = None,
    ):
        # The ID of the region.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        return self


class DescribeDdosCreditResponseBodyDdosCredit(TeaModel):
    def __init__(
        self,
        blackhole_time: int = None,
        score: int = None,
        score_level: str = None,
    ):
        # The time period after which blackhole filtering is automatically deactivated in the specified region. Unit: minutes.
        self.blackhole_time = blackhole_time
        # The security credit score. The full score is **1000**.
        self.score = score
        # The security credit level. Valid values:
        # 
        # *   **A**: outstanding
        # *   **B**: excellent
        # *   **C**: good
        # *   **D**: average
        # *   **E**: poor
        # *   **F**: poorer
        self.score_level = score_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackhole_time is not None:
            result['BlackholeTime'] = self.blackhole_time
        if self.score is not None:
            result['Score'] = self.score
        if self.score_level is not None:
            result['ScoreLevel'] = self.score_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackholeTime') is not None:
            self.blackhole_time = m.get('BlackholeTime')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ScoreLevel') is not None:
            self.score_level = m.get('ScoreLevel')
        return self


class DescribeDdosCreditResponseBody(TeaModel):
    def __init__(
        self,
        ddos_credit: DescribeDdosCreditResponseBodyDdosCredit = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the security credit score of the current Alibaba Cloud account in the specified region.
        self.ddos_credit = ddos_credit
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success

    def validate(self):
        if self.ddos_credit:
            self.ddos_credit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_credit is not None:
            result['DdosCredit'] = self.ddos_credit.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosCredit') is not None:
            temp_model = DescribeDdosCreditResponseBodyDdosCredit()
            self.ddos_credit = temp_model.from_map(m['DdosCredit'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDdosCreditResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDdosCreditResponseBody = None,
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
            temp_model = DescribeDdosCreditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosEventListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        ddos_region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_ip: str = None,
        page_size: int = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The region ID of the asset to query.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The ID of asset to query.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/354191.html) operation to query the IDs of ECS instances, SLB instances, and EIPs within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the asset to query. Valid values:
        # 
        # *   **ecs**: an Elastic Compute Service (ECS) instance.
        # *   **slb**: a Server Load Balancer (SLB) instance.
        # *   **eip**: an elastic IP address (EIP).
        # *   **ipv6**: an IPv6 gateway.
        # *   **swas**: a simple application server.
        # *   **waf**: a Web Application Firewall (WAF) instance of the Exclusive edition.
        # *   **ga_basic**: a Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The IP address of the asset to query.
        self.internet_ip = internet_ip
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDdosEventListResponseBodyDdosEventListDdosEvent(TeaModel):
    def __init__(
        self,
        ddos_status: str = None,
        ddos_type: str = None,
        delay_time: int = None,
        end_time: int = None,
        start_time: int = None,
        un_blackhole_time: int = None,
    ):
        # The status of the DDoS attack event. Valid values:
        # 
        # *   **mitigating**: indicates that traffic scrubbing is in progress.
        # *   **blackholed**: indicates that blackhole filtering is triggered for the asset.
        # *   **normal**: indicates that the DDoS attack event ends.
        self.ddos_status = ddos_status
        # The type of the DDoS attack event. Valid values:
        # 
        # *   **defense**: an attack event that triggers traffic scrubbing
        # *   **blackhole**: an attack event that triggers blackhole filtering
        self.ddos_type = ddos_type
        # The time of the last attack. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > This parameter is returned only when the asset is attacked multiple times within a DDoS attack event.
        self.delay_time = delay_time
        # The end time of the DDoS attack event. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The start time of the DDoS attack event. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The time when blackhole filtering is deactivated. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > This parameter is returned only when the value of the **DdosType** parameter is **blackhole**.
        self.un_blackhole_time = un_blackhole_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.un_blackhole_time is not None:
            result['UnBlackholeTime'] = self.un_blackhole_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UnBlackholeTime') is not None:
            self.un_blackhole_time = m.get('UnBlackholeTime')
        return self


class DescribeDdosEventListResponseBodyDdosEventList(TeaModel):
    def __init__(
        self,
        ddos_event: List[DescribeDdosEventListResponseBodyDdosEventListDdosEvent] = None,
    ):
        self.ddos_event = ddos_event

    def validate(self):
        if self.ddos_event:
            for k in self.ddos_event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DdosEvent'] = []
        if self.ddos_event is not None:
            for k in self.ddos_event:
                result['DdosEvent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ddos_event = []
        if m.get('DdosEvent') is not None:
            for k in m.get('DdosEvent'):
                temp_model = DescribeDdosEventListResponseBodyDdosEventListDdosEvent()
                self.ddos_event.append(temp_model.from_map(k))
        return self


class DescribeDdosEventListResponseBody(TeaModel):
    def __init__(
        self,
        ddos_event_list: DescribeDdosEventListResponseBodyDdosEventList = None,
        request_id: str = None,
        total: int = None,
    ):
        # The details of the DDoS attack events.
        self.ddos_event_list = ddos_event_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of DDoS attack events.
        self.total = total

    def validate(self):
        if self.ddos_event_list:
            self.ddos_event_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_event_list is not None:
            result['DdosEventList'] = self.ddos_event_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosEventList') is not None:
            temp_model = DescribeDdosEventListResponseBodyDdosEventList()
            self.ddos_event_list = temp_model.from_map(m['DdosEventList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDdosEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDdosEventListResponseBody = None,
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
            temp_model = DescribeDdosEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosThresholdRequest(TeaModel):
    def __init__(
        self,
        ddos_region_id: str = None,
        ddos_type: str = None,
        instance_ids: List[str] = None,
        instance_type: str = None,
    ):
        # The region ID of the asset.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The type of the threshold. Valid values:
        # 
        # *   **defense**: traffic scrubbing threshold
        # *   **blackhole**: DDoS mitigation threshold
        # 
        # This parameter is required.
        self.ddos_type = ddos_type
        # The ID of asset N to query.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The type of the asset that is assigned a public IP address. Valid values:
        # 
        # *   **ecs**: ECS instances.
        # *   **slb**: SLB instances.
        # *   **eip**: EIPs.
        # *   **ipv6**: IPv6 gateways.
        # *   **swas**: simple application servers.
        # *   **waf**: Web Application Firewall (WAF) instances of the Exclusive edition.
        # *   **ga_basic**: Global Accelerator (GA) instances.
        # 
        # This parameter is required.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeDdosThresholdResponseBodyThresholdsThreshold(TeaModel):
    def __init__(
        self,
        bps: int = None,
        ddos_type: str = None,
        elastic_bps: int = None,
        instance_id: str = None,
        internet_ip: str = None,
        is_auto: bool = None,
        max_bps: int = None,
        max_pps: int = None,
        pps: int = None,
    ):
        # If the value of the **DdosType** parameter is **defense**, the Bps parameter indicates the current traffic scrubbing threshold. Unit: Mbit/s.
        # 
        # If the value of the **DdosType** parameter is **blackhole**, the Bps parameter indicates the basic protection threshold. Unit: Mbit/s.
        self.bps = bps
        # The type of the threshold. Valid values:
        # 
        # *   **defense**: traffic scrubbing threshold
        # *   **blackhole**: DDoS mitigation threshold
        self.ddos_type = ddos_type
        # The burstable protection threshold (the maximum DDoS mitigation threshold). Unit: Mbit/s.
        # 
        # > This parameter is returned only when the value of the **DdosType** parameter is **blackhole**.
        self.elastic_bps = elastic_bps
        # The ID of the instance.
        self.instance_id = instance_id
        # The IP address of the asset.
        self.internet_ip = internet_ip
        # Indicates whether the threshold is automatically adjusted. Valid values:
        # 
        # *   **true**: The scrubbing thresholds are automatically adjusted based on the traffic load on the asset.
        # *   **false**: The scrubbing thresholds are not automatically adjusted. You must manually specify the scrubbing thresholds.
        self.is_auto = is_auto
        # The maximum traffic scrubbing threshold. Unit: Mbit/s.
        self.max_bps = max_bps
        # The maximum packet scrubbing threshold. Unit: pps.
        self.max_pps = max_pps
        # The packet scrubbing threshold. Unit: pps.
        # 
        # > This parameter is returned only when the value of the **DdosType** parameter is **defense**.
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.elastic_bps is not None:
            result['ElasticBps'] = self.elastic_bps
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_pps is not None:
            result['MaxPps'] = self.max_pps
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('ElasticBps') is not None:
            self.elastic_bps = m.get('ElasticBps')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxPps') is not None:
            self.max_pps = m.get('MaxPps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeDdosThresholdResponseBodyThresholds(TeaModel):
    def __init__(
        self,
        threshold: List[DescribeDdosThresholdResponseBodyThresholdsThreshold] = None,
    ):
        self.threshold = threshold

    def validate(self):
        if self.threshold:
            for k in self.threshold:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Threshold'] = []
        if self.threshold is not None:
            for k in self.threshold:
                result['Threshold'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.threshold = []
        if m.get('Threshold') is not None:
            for k in m.get('Threshold'):
                temp_model = DescribeDdosThresholdResponseBodyThresholdsThreshold()
                self.threshold.append(temp_model.from_map(k))
        return self


class DescribeDdosThresholdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        thresholds: DescribeDdosThresholdResponseBodyThresholds = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the details of the threshold.
        self.thresholds = thresholds

    def validate(self):
        if self.thresholds:
            self.thresholds.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.thresholds is not None:
            result['Thresholds'] = self.thresholds.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Thresholds') is not None:
            temp_model = DescribeDdosThresholdResponseBodyThresholds()
            self.thresholds = temp_model.from_map(m['Thresholds'])
        return self


class DescribeDdosThresholdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDdosThresholdResponseBody = None,
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
            temp_model = DescribeDdosThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        ddos_region_id: str = None,
        ddos_status: str = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_name: str = None,
        instance_type: str = None,
        page_size: int = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The region ID of the asset.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The DDoS mitigation status of the asset. Valid values:
        # 
        # *   **mitigating**: queries assets for which traffic scrubbing is triggered.
        # *   **blackholed**: queries assets for which blackhole filtering is triggered.
        # *   **normal**: queries assets that are not under DDoS attacks.
        self.ddos_status = ddos_status
        # The ID of the asset. The formats of asset IDs vary based on the value of the **InstanceType**. parameter.
        # 
        # *   If you set **InstanceType** to **ecs**, specify the ID of the ECS instance. For example, you can specify i-bp1cb6x80tfgocid\\*\\*\\*\\*.
        # *   If you set **InstanceType** to **slb**, specify the ID of the SLB instance. For example, you can specify alb-vn2dqg3v31y2vd\\*\\*\\*\\*.
        # *   If you set **InstanceType** to **eip**, specify the ID of the EIP. For example, you can specify eip-j6ce6dcx9epi7rs46\\*\\*\\*\\*.
        self.instance_id = instance_id
        # The IP address of the asset.
        self.instance_ip = instance_ip
        # The name of the asset.
        self.instance_name = instance_name
        # The type of the asset to query. Valid values:
        # 
        # *   **ecs**: ECS instances.
        # *   **slb**: SLB instances.
        # *   **eip**: EIPs.
        # *   **ipv6**: IPv6 gateways.
        # *   **swas**: simple application servers.
        # *   **waf**: Web Application Firewall (WAF) instances of the Exclusive edition.
        # *   **ga_basic**: Global Accelerator (GA) instances.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeInstanceResponseBodyInstanceListInstance(TeaModel):
    def __init__(
        self,
        blackhole_threshold: int = None,
        defense_bps_threshold: int = None,
        defense_pps_threshold: int = None,
        elastic_threshold: int = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        ip_version: str = None,
        is_bgppack: bool = None,
    ):
        # The basic protection threshold for the asset. Unit: Mbit/s.
        self.blackhole_threshold = blackhole_threshold
        # The traffic scrubbing threshold for the asset. Unit: Mbit/s.
        self.defense_bps_threshold = defense_bps_threshold
        # The packet scrubbing threshold for the asset. Unit: packets per second (pps).
        self.defense_pps_threshold = defense_pps_threshold
        # The burstable protection threshold for the asset. Unit: Mbit/s.
        self.elastic_threshold = elastic_threshold
        # The ID of the asset.
        self.instance_id = instance_id
        # The IP address of the asset.
        self.instance_ip = instance_ip
        # The name of the asset.
        self.instance_name = instance_name
        # The DDoS mitigation status of the asset. Valid values:
        # 
        # *   **mitigating**: indicates that traffic scrubbing is triggered for the asset.
        # *   **blackholed**: indicates that blackhole filtering is triggered for the asset.
        # *   **normal**: indicates that the instance is normal.
        self.instance_status = instance_status
        # The type of the asset.
        self.instance_type = instance_type
        # The IP protocol that is supported by the asset. Valid values:
        # 
        # *   **v4**: IPv4
        # *   **v6**: IPv6
        self.ip_version = ip_version
        # Indicates whether the asset is associated with an Anti-DDoS Origin Basic instance. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_bgppack = is_bgppack

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackhole_threshold is not None:
            result['BlackholeThreshold'] = self.blackhole_threshold
        if self.defense_bps_threshold is not None:
            result['DefenseBpsThreshold'] = self.defense_bps_threshold
        if self.defense_pps_threshold is not None:
            result['DefensePpsThreshold'] = self.defense_pps_threshold
        if self.elastic_threshold is not None:
            result['ElasticThreshold'] = self.elastic_threshold
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.is_bgppack is not None:
            result['IsBgppack'] = self.is_bgppack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackholeThreshold') is not None:
            self.blackhole_threshold = m.get('BlackholeThreshold')
        if m.get('DefenseBpsThreshold') is not None:
            self.defense_bps_threshold = m.get('DefenseBpsThreshold')
        if m.get('DefensePpsThreshold') is not None:
            self.defense_pps_threshold = m.get('DefensePpsThreshold')
        if m.get('ElasticThreshold') is not None:
            self.elastic_threshold = m.get('ElasticThreshold')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IsBgppack') is not None:
            self.is_bgppack = m.get('IsBgppack')
        return self


class DescribeInstanceResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        instance: List[DescribeInstanceResponseBodyInstanceListInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeInstanceResponseBodyInstanceListInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_list: DescribeInstanceResponseBodyInstanceList = None,
        request_id: str = None,
        total: int = None,
    ):
        # The details of the assets.
        self.instance_list = instance_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of the assets.
        self.total = total

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceList') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceList()
            self.instance_list = temp_model.from_map(m['InstanceList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceResponseBody = None,
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceIpAddressRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        ddos_region_id: str = None,
        ddos_status: str = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_name: str = None,
        instance_type: str = None,
        page_size: int = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The region ID of the asset.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The DDoS mitigation status of the asset. Valid values:
        # 
        # *   **defense**: queries assets for which traffic scrubbing is performed.
        # *   **blackhole**: queries assets for which blackhole filtering is triggered.
        self.ddos_status = ddos_status
        # The ID of the instance to which the asset is added.
        self.instance_id = instance_id
        # The IP address of the asset.
        self.instance_ip = instance_ip
        # The name of the asset.
        self.instance_name = instance_name
        # The type of the asset that is assigned a public IP address. Valid values:
        # 
        # *   **ecs**: ECS instances.
        # *   **slb**: SLB instances.
        # *   **eip**: EIPs.
        # *   **ipv6**: IPv6 gateways.
        # *   **swas**: simple application servers.
        # *   **waf**: Web Application Firewall (WAF) instances of the Exclusive edition.
        # *   **ga_basic**: Global Accelerator (GA) instances.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeInstanceIpAddressResponseBodyInstanceListIpAddressConfig(TeaModel):
    def __init__(
        self,
        blackhole_threshold: int = None,
        defense_bps_threshold: int = None,
        defense_pps_threshold: int = None,
        elastic_threshold: int = None,
        instance_ip: str = None,
        ip_status: str = None,
        ip_version: str = None,
        is_bgppack: bool = None,
        is_full_protection: int = None,
        region_id: str = None,
    ):
        # The basic protection threshold for the asset. Unit: Mbit/s.
        self.blackhole_threshold = blackhole_threshold
        # The traffic scrubbing threshold for the asset measured in Mbit/s. Unit: Mbit/s.
        self.defense_bps_threshold = defense_bps_threshold
        # The traffic scrubbing threshold for the asset measured in packets per second (PPS). Unit: PPS.
        self.defense_pps_threshold = defense_pps_threshold
        # The burstable protection threshold for the asset. Unit: Mbit/s.
        self.elastic_threshold = elastic_threshold
        # The IP address of the asset.
        self.instance_ip = instance_ip
        # The DDoS mitigation status of the asset. Valid values:
        # 
        # *   **mitigating**: indicates that traffic scrubbing is in progress.
        # *   **blackholed**: indicates that blackhole filtering is triggered for the asset.
        # *   **normal**: indicates that no DDoS attacks are launched against the asset.
        self.ip_status = ip_status
        # The IP version of the IP address. Valid values:
        # 
        # *   **v4**: IPv4.
        # *   **v6**: IPv6.
        self.ip_version = ip_version
        # Indicates whether the asset is added to the instance. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_bgppack = is_bgppack
        # Indicates whether best-effort protection is enabled for the asset. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        self.is_full_protection = is_full_protection
        # The region code of the asset.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackhole_threshold is not None:
            result['BlackholeThreshold'] = self.blackhole_threshold
        if self.defense_bps_threshold is not None:
            result['DefenseBpsThreshold'] = self.defense_bps_threshold
        if self.defense_pps_threshold is not None:
            result['DefensePpsThreshold'] = self.defense_pps_threshold
        if self.elastic_threshold is not None:
            result['ElasticThreshold'] = self.elastic_threshold
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.ip_status is not None:
            result['IpStatus'] = self.ip_status
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.is_bgppack is not None:
            result['IsBgppack'] = self.is_bgppack
        if self.is_full_protection is not None:
            result['IsFullProtection'] = self.is_full_protection
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackholeThreshold') is not None:
            self.blackhole_threshold = m.get('BlackholeThreshold')
        if m.get('DefenseBpsThreshold') is not None:
            self.defense_bps_threshold = m.get('DefenseBpsThreshold')
        if m.get('DefensePpsThreshold') is not None:
            self.defense_pps_threshold = m.get('DefensePpsThreshold')
        if m.get('ElasticThreshold') is not None:
            self.elastic_threshold = m.get('ElasticThreshold')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('IpStatus') is not None:
            self.ip_status = m.get('IpStatus')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IsBgppack') is not None:
            self.is_bgppack = m.get('IsBgppack')
        if m.get('IsFullProtection') is not None:
            self.is_full_protection = m.get('IsFullProtection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceIpAddressResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        ip_address_config: List[DescribeInstanceIpAddressResponseBodyInstanceListIpAddressConfig] = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The DDoS mitigation status of the instance. Valid values:
        # 
        # *   **normal**: not under DDoS attacks.
        # *   **abnormal**: under DDoS attacks.
        self.instance_status = instance_status
        # The type of the asset. Valid values:
        # 
        # *   **ecs**\
        # *   **slb**\
        # *   **eip**\
        self.instance_type = instance_type
        # An array that consists of the details of the asset.
        self.ip_address_config = ip_address_config

    def validate(self):
        if self.ip_address_config:
            for k in self.ip_address_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        result['IpAddressConfig'] = []
        if self.ip_address_config is not None:
            for k in self.ip_address_config:
                result['IpAddressConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        self.ip_address_config = []
        if m.get('IpAddressConfig') is not None:
            for k in m.get('IpAddressConfig'):
                temp_model = DescribeInstanceIpAddressResponseBodyInstanceListIpAddressConfig()
                self.ip_address_config.append(temp_model.from_map(k))
        return self


class DescribeInstanceIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        instance_list: List[DescribeInstanceIpAddressResponseBodyInstanceList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # An array that consists of details of the instance.
        self.instance_list = instance_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of the assets.
        self.total = total

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = DescribeInstanceIpAddressResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeInstanceIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceIpAddressResponseBody = None,
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
            temp_model = DescribeInstanceIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpDdosThresholdRequest(TeaModel):
    def __init__(
        self,
        ddos_region_id: str = None,
        ddos_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_ip: str = None,
    ):
        # The region ID of the asset.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The type of the threshold. Valid values:
        # 
        # *   **defense**: traffic scrubbing threshold
        # *   **blackhole**: DDoS mitigation threshold
        # 
        # This parameter is required.
        self.ddos_type = ddos_type
        # The ID of the asset.
        # 
        # > You can call the [DescribeInstanceIpAddress](https://help.aliyun.com/document_detail/429562.html) operation to query the IDs of ECS instances, SLB instances, and EIPs within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the asset that is assigned a public IP address. Valid values:
        # 
        # *   **ecs**: ECS instances.
        # *   **slb**: SLB instances.
        # *   **eip**: EIPs.
        # *   **ipv6**: IPv6 gateways.
        # *   **swas**: simple application servers.
        # *   **waf**: Web Application Firewall (WAF) instances of the Exclusive edition.
        # *   **ga_basic**: Global Accelerator (GA) instances.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The IP address of the asset.
        # 
        # This parameter is required.
        self.internet_ip = internet_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        return self


class DescribeIpDdosThresholdResponseBodyThreshold(TeaModel):
    def __init__(
        self,
        bps: int = None,
        ddos_type: str = None,
        elastic_bps: int = None,
        instance_id: str = None,
        internet_ip: str = None,
        is_auto: bool = None,
        max_bps: int = None,
        max_pps: int = None,
        pps: int = None,
    ):
        # If the value of the **DdosType** parameter is **defense**, the Bps parameter indicates the current traffic scrubbing threshold. Unit: Mbit/s.
        # 
        # If the value of the **DdosType** parameter is **blackhole**, the Bps parameter indicates the basic protection threshold. Unit: Mbit/s.
        self.bps = bps
        # The type of the threshold. Valid values:
        # 
        # *   **defense**: traffic scrubbing threshold
        # *   **blackhole**: DDoS mitigation threshold
        self.ddos_type = ddos_type
        # The burstable protection threshold (the maximum DDoS mitigation threshold). Unit: Mbit/s.
        # 
        # > This parameter is returned only when the value of the **DdosType** parameter is **blackhole**.
        self.elastic_bps = elastic_bps
        # The ID of the instance.
        self.instance_id = instance_id
        # The IP address of the asset.
        self.internet_ip = internet_ip
        # Indicates whether the threshold is automatically adjusted. Valid values:
        # 
        # *   **true**: The scrubbing thresholds are automatically adjusted based on the traffic load on the asset.
        # *   **false**: The scrubbing thresholds are not automatically adjusted. You must manually specify the scrubbing thresholds.
        self.is_auto = is_auto
        # The maximum traffic scrubbing threshold. Unit: Mbit/s.
        self.max_bps = max_bps
        # The maximum packet scrubbing threshold. Unit: pps.
        self.max_pps = max_pps
        # The packet scrubbing threshold. Unit: packets per second (pps).
        # 
        # > This parameter is returned only when the value of the **DdosType** parameter is **defense**.
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.elastic_bps is not None:
            result['ElasticBps'] = self.elastic_bps
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_pps is not None:
            result['MaxPps'] = self.max_pps
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('ElasticBps') is not None:
            self.elastic_bps = m.get('ElasticBps')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxPps') is not None:
            self.max_pps = m.get('MaxPps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeIpDdosThresholdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        threshold: DescribeIpDdosThresholdResponseBodyThreshold = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the details of the threshold.
        self.threshold = threshold

    def validate(self):
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.threshold is not None:
            result['Threshold'] = self.threshold.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Threshold') is not None:
            temp_model = DescribeIpDdosThresholdResponseBodyThreshold()
            self.threshold = temp_model.from_map(m['Threshold'])
        return self


class DescribeIpDdosThresholdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIpDdosThresholdResponseBody = None,
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
            temp_model = DescribeIpDdosThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpLocationServiceRequest(TeaModel):
    def __init__(
        self,
        internet_ip: str = None,
    ):
        # The IP address of the asset to query.
        # 
        # This parameter is required.
        self.internet_ip = internet_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        return self


class DescribeIpLocationServiceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_ip: str = None,
        region: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The type of the asset. Valid values:
        # 
        # *   **ecs**: an ECS instance.
        # *   **slb**: an SLB instance.
        # *   **eip**: an EIP.
        # *   **ipv6**: an IPv6 gateway.
        # *   **swas**: a simple application server.
        # *   **waf**: a Web Application Firewall (WAF) instance of the Exclusive edition.
        # *   **ga_basic**: a Global Accelerator (GA) instance.
        self.instance_type = instance_type
        # The IP address of the asset.
        self.internet_ip = internet_ip
        # The region to which the public IP address of the asset belongs.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeIpLocationServiceResponseBody(TeaModel):
    def __init__(
        self,
        instance: DescribeIpLocationServiceResponseBodyInstance = None,
        request_id: str = None,
    ):
        # The details of the asset.
        self.instance = instance
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = DescribeIpLocationServiceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIpLocationServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIpLocationServiceResponseBody = None,
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
            temp_model = DescribeIpLocationServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_en_name: str = None,
        region_name: str = None,
        region_no: str = None,
        region_no_alias: str = None,
    ):
        # The English name of the region.
        self.region_en_name = region_en_name
        # The Chinese name of the region.
        self.region_name = region_name
        # The code of the region.
        self.region_no = region_no
        # The ID of the region.
        self.region_no_alias = region_no_alias

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_en_name is not None:
            result['RegionEnName'] = self.region_en_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.region_no_alias is not None:
            result['RegionNoAlias'] = self.region_no_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEnName') is not None:
            self.region_en_name = m.get('RegionEnName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RegionNoAlias') is not None:
            self.region_no_alias = m.get('RegionNoAlias')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        # An array consisting of regions in which Anti-DDoS Origin Basic is available.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
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


class ModifyDefenseThresholdRequest(TeaModel):
    def __init__(
        self,
        bps: int = None,
        client_token: str = None,
        ddos_region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_ip: str = None,
        is_auto: bool = None,
        pps: int = None,
    ):
        # The traffic scrubbing threshold. Unit: Mbit/s. The traffic scrubbing threshold cannot exceed the peak inbound or outbound Internet traffic, whichever is larger, of the asset. When you modify Bps, Pps is required. Otherwise, Bps does not take effect.
        # 
        # You can use the monitoring tool that is provided by the asset to query the Internet traffic of the asset:
        # 
        # *   If the asset is an ECS instance, see [View instance monitoring information](https://help.aliyun.com/document_detail/25482.html).
        # *   If the asset is an SLB instance, see [View monitoring data](https://help.aliyun.com/document_detail/85982.html).
        self.bps = bps
        self.client_token = client_token
        # The region ID of the asset for which you want to change the scrubbing thresholds.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The ID of the asset.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/354191.html) operation to query the IDs of ECS instances, SLB instances, and EIPs within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the asset. Valid values:
        # 
        # *   **ecs**: an Elastic Compute Service (ECS) instance.
        # *   **slb**: a Server Load Balancer (SLB) instance.
        # *   **eip**: an elastic IP address (EIP).
        # *   **ipv6**: an IPv6 gateway.
        # *   **swas**: a simple application server.
        # *   **waf**: a Web Application Firewall (WAF) instance of the Exclusive edition.
        # *   **ga_basic**: a Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The IP address of the asset.
        self.internet_ip = internet_ip
        # Specifies whether to automatically adjust the scrubbing threshold based on the traffic load on the asset. Valid values:
        # 
        # *   **true**: automatically adjusts the scrubbing thresholds. You do not need to configure the **Bps** and **Pps** parameters.
        # *   **false**: The scrubbing threshold is not automatically adjusted. You must configure the **Bps** and **Pps** parameters.
        # 
        # Default value: false.
        self.is_auto = is_auto
        # The packet scrubbing threshold. Unit: packets per second (PPS). When you modify Pps, Bps is required. Otherwise, Pps does not take effect.
        # 
        # The packet scrubbing threshold cannot exceed the peak number of inbound or outbound packets, whichever is larger, of the asset. You can use the monitoring tool that is provided by the asset to query the number of packets of the asset:
        # 
        # *   If the asset is an ECS instance, see [View instance monitoring information](https://help.aliyun.com/document_detail/25482.html).
        # *   If the asset is an SLB instance, see [View monitoring data](https://help.aliyun.com/document_detail/85982.html).
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class ModifyDefenseThresholdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDefenseThresholdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDefenseThresholdResponseBody = None,
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
            temp_model = ModifyDefenseThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpDefenseThresholdRequest(TeaModel):
    def __init__(
        self,
        bps: int = None,
        ddos_region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_ip: str = None,
        is_auto: bool = None,
        pps: int = None,
    ):
        # The traffic scrubbing threshold. Unit: Mbit/s. The traffic scrubbing threshold cannot exceed the peak inbound or outbound Internet traffic, whichever is larger, of the asset. When you modify Bps, Pps is required. Otherwise, Bps does not take effect.
        # 
        # You can use the monitoring tool that is provided by the asset to query the Internet traffic of the asset:
        # 
        # *   If the asset is an ECS instance, see [View instance monitoring information](https://help.aliyun.com/document_detail/25482.html).
        # *   If the asset is an SLB instance, see [View monitoring data](https://help.aliyun.com/document_detail/85982.html).
        # *   If the asset is an EIP, see [View monitoring data](https://help.aliyun.com/document_detail/85354.html).
        self.bps = bps
        # The region ID of the asset.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The ID of the asset.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/354191.html) operation to query the IDs of ECS instances, SLB instances, and EIPs within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the asset. Valid values:
        # 
        # *   **ecs**: an Elastic Compute Service (ECS) instance.
        # *   **slb**: a Server Load Balancer (SLB) instance.
        # *   **eip**: an elastic IP address (EIP).
        # *   **ipv6**: an IPv6 gateway.
        # *   **swas**: a simple application server.
        # *   **waf**: a Web Application Firewall (WAF) instance of the Exclusive edition.
        # *   **ga_basic**: a Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The IP address of the asset.
        # 
        # This parameter is required.
        self.internet_ip = internet_ip
        # Specifies whether to automatically adjust the scrubbing threshold based on the traffic load on the asset. Valid values:
        # 
        # *   **true**: automatically adjusts the scrubbing threshold. You do not need to configure the **Bps** and **Pps** parameters.
        # *   **false**: The scrubbing threshold is not automatically adjusted. You must configure the **Bps** and **Pps** parameters. This is the default value.
        self.is_auto = is_auto
        # The packet scrubbing threshold. Unit: packets per second (PPS). When you modify Pps, Bps is required. Otherwise, Pps does not take effect.
        # 
        # The packet scrubbing threshold cannot exceed the peak number of inbound or outbound packets, whichever is larger, of the asset. You can use the monitoring tool that is provided by the asset to query the number of packets of the asset:
        # 
        # *   If the asset is an ECS instance, see [View instance monitoring information](https://help.aliyun.com/document_detail/25482.html).
        # *   If the asset is an SLB instance, see [View monitoring data](https://help.aliyun.com/document_detail/85982.html).
        # *   If the asset is an EIP, see [View monitoring data](https://help.aliyun.com/document_detail/85354.html).
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class ModifyIpDefenseThresholdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyIpDefenseThresholdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyIpDefenseThresholdResponseBody = None,
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
            temp_model = ModifyIpDefenseThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


