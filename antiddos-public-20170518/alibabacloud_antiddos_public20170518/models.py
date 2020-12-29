# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DescribeBgpPackByIpRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ddos_region_id: str = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ddos_region_id = ddos_region_id
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeBgpPackByIpResponseBodyDdosbgpInfo(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        elastic_threshold: int = None,
        ip: str = None,
        base_threshold: int = None,
        ddosbgp_instance_id: str = None,
    ):
        self.expire_time = expire_time
        self.elastic_threshold = elastic_threshold
        self.ip = ip
        self.base_threshold = base_threshold
        self.ddosbgp_instance_id = ddosbgp_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.elastic_threshold is not None:
            result['ElasticThreshold'] = self.elastic_threshold
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.base_threshold is not None:
            result['BaseThreshold'] = self.base_threshold
        if self.ddosbgp_instance_id is not None:
            result['DdosbgpInstanceId'] = self.ddosbgp_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ElasticThreshold') is not None:
            self.elastic_threshold = m.get('ElasticThreshold')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('BaseThreshold') is not None:
            self.base_threshold = m.get('BaseThreshold')
        if m.get('DdosbgpInstanceId') is not None:
            self.ddosbgp_instance_id = m.get('DdosbgpInstanceId')
        return self


class DescribeBgpPackByIpResponseBody(TeaModel):
    def __init__(
        self,
        ddosbgp_info: DescribeBgpPackByIpResponseBodyDdosbgpInfo = None,
        request_id: str = None,
    ):
        self.ddosbgp_info = ddosbgp_info
        self.request_id = request_id

    def validate(self):
        if self.ddosbgp_info:
            self.ddosbgp_info.validate()

    def to_map(self):
        result = dict()
        if self.ddosbgp_info is not None:
            result['DdosbgpInfo'] = self.ddosbgp_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosbgpInfo') is not None:
            temp_model = DescribeBgpPackByIpResponseBodyDdosbgpInfo()
            self.ddosbgp_info = temp_model.from_map(m['DdosbgpInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBgpPackByIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBgpPackByIpResponseBody = None,
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
            temp_model = DescribeBgpPackByIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBgpPackElasticThresholdRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ddos_region_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ddos_region_id = ddos_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        return self


class DescribeBgpPackElasticThresholdResponseBody(TeaModel):
    def __init__(
        self,
        max_threshold: int = None,
        request_id: str = None,
        openable: bool = None,
    ):
        self.max_threshold = max_threshold
        self.request_id = request_id
        self.openable = openable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_threshold is not None:
            result['MaxThreshold'] = self.max_threshold
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.openable is not None:
            result['Openable'] = self.openable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxThreshold') is not None:
            self.max_threshold = m.get('MaxThreshold')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Openable') is not None:
            self.openable = m.get('Openable')
        return self


class DescribeBgpPackElasticThresholdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBgpPackElasticThresholdResponseBody = None,
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
            temp_model = DescribeBgpPackElasticThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCapRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ddos_region_id: str = None,
        instance_type: str = None,
        instance_id: str = None,
        beg_time: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ddos_region_id = ddos_region_id
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.beg_time = beg_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.beg_time is not None:
            result['BegTime'] = self.beg_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BegTime') is not None:
            self.beg_time = m.get('BegTime')
        return self


class DescribeCapResponseBodyCapUrl(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
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
        self.cap_url = cap_url
        self.request_id = request_id

    def validate(self):
        if self.cap_url:
            self.cap_url.validate()

    def to_map(self):
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
        body: DescribeCapResponseBody = None,
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
            temp_model = DescribeCapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCreditInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeCreditInfoResponseBody(TeaModel):
    def __init__(
        self,
        punish_times: int = None,
        last_order_time: int = None,
        last_login_time: int = None,
        request_id: str = None,
        user_level: str = None,
        black_times: int = None,
        new_createtime: str = None,
        duration: int = None,
        productid: List[str] = None,
    ):
        self.punish_times = punish_times
        self.last_order_time = last_order_time
        self.last_login_time = last_login_time
        self.request_id = request_id
        self.user_level = user_level
        self.black_times = black_times
        self.new_createtime = new_createtime
        self.duration = duration
        self.productid = productid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.punish_times is not None:
            result['PunishTimes'] = self.punish_times
        if self.last_order_time is not None:
            result['LastOrderTime'] = self.last_order_time
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_level is not None:
            result['UserLevel'] = self.user_level
        if self.black_times is not None:
            result['BlackTimes'] = self.black_times
        if self.new_createtime is not None:
            result['NewCreatetime'] = self.new_createtime
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.productid is not None:
            result['Productid'] = self.productid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PunishTimes') is not None:
            self.punish_times = m.get('PunishTimes')
        if m.get('LastOrderTime') is not None:
            self.last_order_time = m.get('LastOrderTime')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserLevel') is not None:
            self.user_level = m.get('UserLevel')
        if m.get('BlackTimes') is not None:
            self.black_times = m.get('BlackTimes')
        if m.get('NewCreatetime') is not None:
            self.new_createtime = m.get('NewCreatetime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Productid') is not None:
            self.productid = m.get('Productid')
        return self


class DescribeCreditInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCreditInfoResponseBody = None,
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
            temp_model = DescribeCreditInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosCountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ddos_region_id: str = None,
        instance_type: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ddos_region_id = ddos_region_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeDdosCountResponseBodyDdosCount(TeaModel):
    def __init__(
        self,
        defense_count: int = None,
        blackhole_count: int = None,
        instacen_count: int = None,
    ):
        self.defense_count = defense_count
        self.blackhole_count = blackhole_count
        self.instacen_count = instacen_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count
        if self.blackhole_count is not None:
            result['BlackholeCount'] = self.blackhole_count
        if self.instacen_count is not None:
            result['InstacenCount'] = self.instacen_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')
        if m.get('BlackholeCount') is not None:
            self.blackhole_count = m.get('BlackholeCount')
        if m.get('InstacenCount') is not None:
            self.instacen_count = m.get('InstacenCount')
        return self


class DescribeDdosCountResponseBody(TeaModel):
    def __init__(
        self,
        ddos_count: DescribeDdosCountResponseBodyDdosCount = None,
        request_id: str = None,
    ):
        self.ddos_count = ddos_count
        self.request_id = request_id

    def validate(self):
        if self.ddos_count:
            self.ddos_count.validate()

    def to_map(self):
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
        body: DescribeDdosCountResponseBody = None,
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
            temp_model = DescribeDdosCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosCreditRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ddos_region_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ddos_region_id = ddos_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        return self


class DescribeDdosCreditResponseBodyDdosCredit(TeaModel):
    def __init__(
        self,
        score: int = None,
        score_level: str = None,
        blackhole_time: int = None,
    ):
        self.score = score
        self.score_level = score_level
        self.blackhole_time = blackhole_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.score_level is not None:
            result['ScoreLevel'] = self.score_level
        if self.blackhole_time is not None:
            result['BlackholeTime'] = self.blackhole_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ScoreLevel') is not None:
            self.score_level = m.get('ScoreLevel')
        if m.get('BlackholeTime') is not None:
            self.blackhole_time = m.get('BlackholeTime')
        return self


class DescribeDdosCreditResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ddos_credit: DescribeDdosCreditResponseBodyDdosCredit = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.ddos_credit = ddos_credit
        self.success = success

    def validate(self):
        if self.ddos_credit:
            self.ddos_credit.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ddos_credit is not None:
            result['DdosCredit'] = self.ddos_credit.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DdosCredit') is not None:
            temp_model = DescribeDdosCreditResponseBodyDdosCredit()
            self.ddos_credit = temp_model.from_map(m['DdosCredit'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDdosCreditResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDdosCreditResponseBody = None,
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
            temp_model = DescribeDdosCreditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosEventListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ddos_region_id: str = None,
        instance_type: str = None,
        instance_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ddos_region_id = ddos_region_id
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDdosEventListResponseBodyDdosEventList(TeaModel):
    def __init__(
        self,
        ddos_type: str = None,
        end_time: int = None,
        start_time: int = None,
        delay_time: int = None,
        ddos_status: str = None,
        un_blackhole_time: int = None,
    ):
        self.ddos_type = ddos_type
        self.end_time = end_time
        self.start_time = start_time
        self.delay_time = delay_time
        self.ddos_status = ddos_status
        self.un_blackhole_time = un_blackhole_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.un_blackhole_time is not None:
            result['UnBlackholeTime'] = self.un_blackhole_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('UnBlackholeTime') is not None:
            self.un_blackhole_time = m.get('UnBlackholeTime')
        return self


class DescribeDdosEventListResponseBody(TeaModel):
    def __init__(
        self,
        ddos_event_list: List[DescribeDdosEventListResponseBodyDdosEventList] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.ddos_event_list = ddos_event_list
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.ddos_event_list:
            for k in self.ddos_event_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DdosEventList'] = []
        if self.ddos_event_list is not None:
            for k in self.ddos_event_list:
                result['DdosEventList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ddos_event_list = []
        if m.get('DdosEventList') is not None:
            for k in m.get('DdosEventList'):
                temp_model = DescribeDdosEventListResponseBodyDdosEventList()
                self.ddos_event_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDdosEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDdosEventListResponseBody = None,
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
            temp_model = DescribeDdosEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosThresholdRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ddos_region_id: str = None,
        ddos_type: str = None,
        instance_type: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ddos_region_id = ddos_region_id
        self.ddos_type = ddos_type
        self.instance_type = instance_type
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeDdosThresholdResponseBodyThresholds(TeaModel):
    def __init__(
        self,
        ddos_type: str = None,
        is_auto: bool = None,
        max_bps: int = None,
        elastic_bps: int = None,
        instance_id: str = None,
        bps: int = None,
        pps: int = None,
        max_pps: int = None,
    ):
        self.ddos_type = ddos_type
        self.is_auto = is_auto
        self.max_bps = max_bps
        self.elastic_bps = elastic_bps
        self.instance_id = instance_id
        self.bps = bps
        self.pps = pps
        self.max_pps = max_pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.elastic_bps is not None:
            result['ElasticBps'] = self.elastic_bps
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.max_pps is not None:
            result['MaxPps'] = self.max_pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('ElasticBps') is not None:
            self.elastic_bps = m.get('ElasticBps')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('MaxPps') is not None:
            self.max_pps = m.get('MaxPps')
        return self


class DescribeDdosThresholdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        thresholds: List[DescribeDdosThresholdResponseBodyThresholds] = None,
    ):
        self.request_id = request_id
        self.thresholds = thresholds

    def validate(self):
        if self.thresholds:
            for k in self.thresholds:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Thresholds'] = []
        if self.thresholds is not None:
            for k in self.thresholds:
                result['Thresholds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.thresholds = []
        if m.get('Thresholds') is not None:
            for k in m.get('Thresholds'):
                temp_model = DescribeDdosThresholdResponseBodyThresholds()
                self.thresholds.append(temp_model.from_map(k))
        return self


class DescribeDdosThresholdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDdosThresholdResponseBody = None,
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
            temp_model = DescribeDdosThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlexibleProtectionFlowRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        days: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.days = days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.days is not None:
            result['Days'] = self.days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        return self


class DescribeFlexibleProtectionFlowResponseBodyFlows(TeaModel):
    def __init__(
        self,
        used_flow: float = None,
        time: int = None,
        add_flow: float = None,
        useable_flow: float = None,
    ):
        self.used_flow = used_flow
        self.time = time
        self.add_flow = add_flow
        self.useable_flow = useable_flow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.used_flow is not None:
            result['UsedFlow'] = self.used_flow
        if self.time is not None:
            result['Time'] = self.time
        if self.add_flow is not None:
            result['AddFlow'] = self.add_flow
        if self.useable_flow is not None:
            result['UseableFlow'] = self.useable_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsedFlow') is not None:
            self.used_flow = m.get('UsedFlow')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('AddFlow') is not None:
            self.add_flow = m.get('AddFlow')
        if m.get('UseableFlow') is not None:
            self.useable_flow = m.get('UseableFlow')
        return self


class DescribeFlexibleProtectionFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        flows: List[DescribeFlexibleProtectionFlowResponseBodyFlows] = None,
    ):
        self.request_id = request_id
        self.flows = flows

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = DescribeFlexibleProtectionFlowResponseBodyFlows()
                self.flows.append(temp_model.from_map(k))
        return self


class DescribeFlexibleProtectionFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlexibleProtectionFlowResponseBody = None,
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
            temp_model = DescribeFlexibleProtectionFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowgraphRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        eagle_eye_trace_id: str = None,
        eagle_eye_rpc_id: str = None,
        eagle_eye_user_data: str = None,
        ddos_region_id: str = None,
        instance_type: str = None,
        instance_id: str = None,
        days: int = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.eagle_eye_trace_id = eagle_eye_trace_id
        self.eagle_eye_rpc_id = eagle_eye_rpc_id
        self.eagle_eye_user_data = eagle_eye_user_data
        self.ddos_region_id = ddos_region_id
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.days = days
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.eagle_eye_trace_id is not None:
            result['eagleEyeTraceId'] = self.eagle_eye_trace_id
        if self.eagle_eye_rpc_id is not None:
            result['eagleEyeRpcId'] = self.eagle_eye_rpc_id
        if self.eagle_eye_user_data is not None:
            result['eagleEyeUserData'] = self.eagle_eye_user_data
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.days is not None:
            result['Days'] = self.days
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('eagleEyeTraceId') is not None:
            self.eagle_eye_trace_id = m.get('eagleEyeTraceId')
        if m.get('eagleEyeRpcId') is not None:
            self.eagle_eye_rpc_id = m.get('eagleEyeRpcId')
        if m.get('eagleEyeUserData') is not None:
            self.eagle_eye_user_data = m.get('eagleEyeUserData')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeFlowgraphResponseBodyFlowgraphs(TeaModel):
    def __init__(
        self,
        time: int = None,
        bps: int = None,
        pps: int = None,
    ):
        self.time = time
        self.bps = bps
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeFlowgraphResponseBody(TeaModel):
    def __init__(
        self,
        flowgraphs: List[DescribeFlowgraphResponseBodyFlowgraphs] = None,
        request_id: str = None,
    ):
        self.flowgraphs = flowgraphs
        self.request_id = request_id

    def validate(self):
        if self.flowgraphs:
            for k in self.flowgraphs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Flowgraphs'] = []
        if self.flowgraphs is not None:
            for k in self.flowgraphs:
                result['Flowgraphs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flowgraphs = []
        if m.get('Flowgraphs') is not None:
            for k in m.get('Flowgraphs'):
                temp_model = DescribeFlowgraphResponseBodyFlowgraphs()
                self.flowgraphs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFlowgraphResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlowgraphResponseBody = None,
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
            temp_model = DescribeFlowgraphResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionDdosThresholdRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ddos_region_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ddos_region_id = ddos_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        return self


class DescribeRegionDdosThresholdResponseBodyRegionDdosThreshold(TeaModel):
    def __init__(
        self,
        elastic_threshold: int = None,
        base_threshold: int = None,
    ):
        self.elastic_threshold = elastic_threshold
        self.base_threshold = base_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.elastic_threshold is not None:
            result['ElasticThreshold'] = self.elastic_threshold
        if self.base_threshold is not None:
            result['BaseThreshold'] = self.base_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticThreshold') is not None:
            self.elastic_threshold = m.get('ElasticThreshold')
        if m.get('BaseThreshold') is not None:
            self.base_threshold = m.get('BaseThreshold')
        return self


class DescribeRegionDdosThresholdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        region_ddos_threshold: DescribeRegionDdosThresholdResponseBodyRegionDdosThreshold = None,
    ):
        self.request_id = request_id
        self.region_ddos_threshold = region_ddos_threshold

    def validate(self):
        if self.region_ddos_threshold:
            self.region_ddos_threshold.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_ddos_threshold is not None:
            result['RegionDdosThreshold'] = self.region_ddos_threshold.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionDdosThreshold') is not None:
            temp_model = DescribeRegionDdosThresholdResponseBodyRegionDdosThreshold()
            self.region_ddos_threshold = temp_model.from_map(m['RegionDdosThreshold'])
        return self


class DescribeRegionDdosThresholdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionDdosThresholdResponseBody = None,
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
            temp_model = DescribeRegionDdosThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_en_name: str = None,
        region_name: str = None,
        region_no: str = None,
        region_no_alias: str = None,
    ):
        self.region_en_name = region_en_name
        self.region_name = region_name
        self.region_no = region_no
        self.region_no_alias = region_no_alias

    def validate(self):
        pass

    def to_map(self):
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


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrafficInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeTrafficInfoResponseBodyTrafficInfo(TeaModel):
    def __init__(
        self,
        last_used_traffic: int = None,
        add_traffic: int = None,
        usable_traffic: int = None,
    ):
        self.last_used_traffic = last_used_traffic
        self.add_traffic = add_traffic
        self.usable_traffic = usable_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.last_used_traffic is not None:
            result['LastUsedTraffic'] = self.last_used_traffic
        if self.add_traffic is not None:
            result['AddTraffic'] = self.add_traffic
        if self.usable_traffic is not None:
            result['UsableTraffic'] = self.usable_traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUsedTraffic') is not None:
            self.last_used_traffic = m.get('LastUsedTraffic')
        if m.get('AddTraffic') is not None:
            self.add_traffic = m.get('AddTraffic')
        if m.get('UsableTraffic') is not None:
            self.usable_traffic = m.get('UsableTraffic')
        return self


class DescribeTrafficInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_info: DescribeTrafficInfoResponseBodyTrafficInfo = None,
    ):
        self.request_id = request_id
        self.traffic_info = traffic_info

    def validate(self):
        if self.traffic_info:
            self.traffic_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_info is not None:
            result['TrafficInfo'] = self.traffic_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficInfo') is not None:
            temp_model = DescribeTrafficInfoResponseBodyTrafficInfo()
            self.traffic_info = temp_model.from_map(m['TrafficInfo'])
        return self


class DescribeTrafficInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTrafficInfoResponseBody = None,
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
            temp_model = DescribeTrafficInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDdosStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ddos_region_id: str = None,
        instance_type: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ddos_region_id = ddos_region_id
        self.instance_type = instance_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyDdosStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDdosStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDdosStatusResponseBody = None,
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
            temp_model = ModifyDdosStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefenseThresholdRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ddos_region_id: str = None,
        instance_type: str = None,
        instance_id: str = None,
        bps: int = None,
        pps: int = None,
        is_auto: bool = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ddos_region_id = ddos_region_id
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.bps = bps
        self.pps = pps
        self.is_auto = is_auto

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')
        return self


class ModifyDefenseThresholdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
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
        body: ModifyDefenseThresholdResponseBody = None,
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
            temp_model = ModifyDefenseThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


