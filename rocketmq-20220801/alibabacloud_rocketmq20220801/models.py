# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConsumerGroupRequestConsumeRetryPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_topic: str = None,
        max_retry_times: int = None,
        retry_policy: str = None,
    ):
        self.dead_letter_target_topic = dead_letter_target_topic
        self.max_retry_times = max_retry_times
        self.retry_policy = retry_policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_topic is not None:
            result['deadLetterTargetTopic'] = self.dead_letter_target_topic
        if self.max_retry_times is not None:
            result['maxRetryTimes'] = self.max_retry_times
        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deadLetterTargetTopic') is not None:
            self.dead_letter_target_topic = m.get('deadLetterTargetTopic')
        if m.get('maxRetryTimes') is not None:
            self.max_retry_times = m.get('maxRetryTimes')
        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')
        return self


class CreateConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        consume_retry_policy: CreateConsumerGroupRequestConsumeRetryPolicy = None,
        delivery_order_type: str = None,
        remark: str = None,
    ):
        self.consume_retry_policy = consume_retry_policy
        self.delivery_order_type = delivery_order_type
        self.remark = remark

    def validate(self):
        if self.consume_retry_policy:
            self.consume_retry_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_retry_policy is not None:
            result['consumeRetryPolicy'] = self.consume_retry_policy.to_map()
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = CreateConsumerGroupRequestConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m['consumeRetryPolicy'])
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConsumerGroupResponseBody = None,
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
            temp_model = CreateConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestNetworkInfoInternetInfo(TeaModel):
    def __init__(
        self,
        flow_out_bandwidth: int = None,
        flow_out_type: str = None,
        internet_spec: str = None,
        ip_whitelist: List[str] = None,
    ):
        self.flow_out_bandwidth = flow_out_bandwidth
        self.flow_out_type = flow_out_type
        self.internet_spec = internet_spec
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth
        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type
        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')
        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')
        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class CreateInstanceRequestNetworkInfoVpcInfo(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class CreateInstanceRequestNetworkInfo(TeaModel):
    def __init__(
        self,
        internet_info: CreateInstanceRequestNetworkInfoInternetInfo = None,
        vpc_info: CreateInstanceRequestNetworkInfoVpcInfo = None,
    ):
        self.internet_info = internet_info
        self.vpc_info = vpc_info

    def validate(self):
        if self.internet_info:
            self.internet_info.validate()
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()
        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internetInfo') is not None:
            temp_model = CreateInstanceRequestNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m['internetInfo'])
        if m.get('vpcInfo') is not None:
            temp_model = CreateInstanceRequestNetworkInfoVpcInfo()
            self.vpc_info = temp_model.from_map(m['vpcInfo'])
        return self


class CreateInstanceRequestProductInfo(TeaModel):
    def __init__(
        self,
        auto_scaling: bool = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        send_receive_ratio: float = None,
    ):
        self.auto_scaling = auto_scaling
        self.message_retention_time = message_retention_time
        self.msg_process_spec = msg_process_spec
        self.send_receive_ratio = send_receive_ratio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        instance_name: str = None,
        network_info: CreateInstanceRequestNetworkInfo = None,
        payment_type: str = None,
        period: int = None,
        period_unit: str = None,
        product_info: CreateInstanceRequestProductInfo = None,
        remark: str = None,
        resource_group_id: str = None,
        series_code: str = None,
        service_code: str = None,
        sub_series_code: str = None,
        client_token: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.instance_name = instance_name
        self.network_info = network_info
        self.payment_type = payment_type
        self.period = period
        self.period_unit = period_unit
        self.product_info = product_info
        self.remark = remark
        self.resource_group_id = resource_group_id
        self.series_code = series_code
        self.service_code = service_code
        self.sub_series_code = sub_series_code
        self.client_token = client_token

    def validate(self):
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['periodUnit'] = self.period_unit
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.remark is not None:
            result['remark'] = self.remark
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_code is not None:
            result['seriesCode'] = self.series_code
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('networkInfo') is not None:
            temp_model = CreateInstanceRequestNetworkInfo()
            self.network_info = temp_model.from_map(m['networkInfo'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodUnit') is not None:
            self.period_unit = m.get('periodUnit')
        if m.get('productInfo') is not None:
            temp_model = CreateInstanceRequestProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTopicRequest(TeaModel):
    def __init__(
        self,
        message_type: str = None,
        remark: str = None,
    ):
        self.message_type = message_type
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTopicResponseBody = None,
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
            temp_model = CreateTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConsumerGroupResponseBody = None,
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
            temp_model = DeleteConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceResponseBody = None,
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTopicResponseBody = None,
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
            temp_model = DeleteTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsumerGroupResponseBodyDataConsumeRetryPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_topic: str = None,
        max_retry_times: int = None,
        retry_policy: str = None,
    ):
        self.dead_letter_target_topic = dead_letter_target_topic
        self.max_retry_times = max_retry_times
        self.retry_policy = retry_policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_topic is not None:
            result['deadLetterTargetTopic'] = self.dead_letter_target_topic
        if self.max_retry_times is not None:
            result['maxRetryTimes'] = self.max_retry_times
        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deadLetterTargetTopic') is not None:
            self.dead_letter_target_topic = m.get('deadLetterTargetTopic')
        if m.get('maxRetryTimes') is not None:
            self.max_retry_times = m.get('maxRetryTimes')
        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')
        return self


class GetConsumerGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        consume_retry_policy: GetConsumerGroupResponseBodyDataConsumeRetryPolicy = None,
        consumer_group_id: str = None,
        create_time: str = None,
        delivery_order_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.consume_retry_policy = consume_retry_policy
        self.consumer_group_id = consumer_group_id
        self.create_time = create_time
        self.delivery_order_type = delivery_order_type
        self.instance_id = instance_id
        self.region_id = region_id
        self.remark = remark
        self.status = status
        self.update_time = update_time

    def validate(self):
        if self.consume_retry_policy:
            self.consume_retry_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_retry_policy is not None:
            result['consumeRetryPolicy'] = self.consume_retry_policy.to_map()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = GetConsumerGroupResponseBodyDataConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m['consumeRetryPolicy'])
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetConsumerGroupResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetConsumerGroupResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConsumerGroupResponseBody = None,
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
            temp_model = GetConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyDataAccountInfo(TeaModel):
    def __init__(
        self,
        username: str = None,
    ):
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetInstanceResponseBodyDataAclInfo(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
    ):
        self.acl_type = acl_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['aclType'] = self.acl_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')
        return self


class GetInstanceResponseBodyDataExtConfig(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
        auto_scaling: bool = None,
        flow_out_bandwidth: int = None,
        flow_out_type: str = None,
        internet_spec: str = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        send_receive_ratio: float = None,
        support_auto_scaling: bool = None,
    ):
        self.acl_type = acl_type
        self.auto_scaling = auto_scaling
        self.flow_out_bandwidth = flow_out_bandwidth
        self.flow_out_type = flow_out_type
        self.internet_spec = internet_spec
        self.message_retention_time = message_retention_time
        self.msg_process_spec = msg_process_spec
        self.send_receive_ratio = send_receive_ratio
        self.support_auto_scaling = support_auto_scaling

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['aclType'] = self.acl_type
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth
        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type
        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        if self.support_auto_scaling is not None:
            result['supportAutoScaling'] = self.support_auto_scaling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')
        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')
        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        if m.get('supportAutoScaling') is not None:
            self.support_auto_scaling = m.get('supportAutoScaling')
        return self


class GetInstanceResponseBodyDataInstanceQuotas(TeaModel):
    def __init__(
        self,
        free_count: float = None,
        quota_name: str = None,
        total_count: float = None,
        used_count: float = None,
    ):
        self.free_count = free_count
        self.quota_name = quota_name
        self.total_count = total_count
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.free_count is not None:
            result['freeCount'] = self.free_count
        if self.quota_name is not None:
            result['quotaName'] = self.quota_name
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.used_count is not None:
            result['usedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('freeCount') is not None:
            self.free_count = m.get('freeCount')
        if m.get('quotaName') is not None:
            self.quota_name = m.get('quotaName')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('usedCount') is not None:
            self.used_count = m.get('usedCount')
        return self


class GetInstanceResponseBodyDataNetworkInfoEndpoints(TeaModel):
    def __init__(
        self,
        endpoint_type: str = None,
        endpoint_url: str = None,
        ip_whitelist: List[str] = None,
    ):
        self.endpoint_type = endpoint_type
        self.endpoint_url = endpoint_url
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['endpointType'] = self.endpoint_type
        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointType') is not None:
            self.endpoint_type = m.get('endpointType')
        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class GetInstanceResponseBodyDataNetworkInfoInternetInfo(TeaModel):
    def __init__(
        self,
        flow_out_bandwidth: int = None,
        flow_out_type: str = None,
        internet_spec: str = None,
        ip_whitelist: List[str] = None,
    ):
        self.flow_out_bandwidth = flow_out_bandwidth
        self.flow_out_type = flow_out_type
        self.internet_spec = internet_spec
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth
        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type
        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')
        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')
        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class GetInstanceResponseBodyDataNetworkInfoVpcInfo(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class GetInstanceResponseBodyDataNetworkInfo(TeaModel):
    def __init__(
        self,
        endpoints: List[GetInstanceResponseBodyDataNetworkInfoEndpoints] = None,
        internet_info: GetInstanceResponseBodyDataNetworkInfoInternetInfo = None,
        vpc_info: GetInstanceResponseBodyDataNetworkInfoVpcInfo = None,
    ):
        self.endpoints = endpoints
        self.internet_info = internet_info
        self.vpc_info = vpc_info

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()
        if self.internet_info:
            self.internet_info.validate()
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['endpoints'].append(k.to_map() if k else None)
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()
        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('endpoints') is not None:
            for k in m.get('endpoints'):
                temp_model = GetInstanceResponseBodyDataNetworkInfoEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('internetInfo') is not None:
            temp_model = GetInstanceResponseBodyDataNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m['internetInfo'])
        if m.get('vpcInfo') is not None:
            temp_model = GetInstanceResponseBodyDataNetworkInfoVpcInfo()
            self.vpc_info = temp_model.from_map(m['vpcInfo'])
        return self


class GetInstanceResponseBodyDataProductInfo(TeaModel):
    def __init__(
        self,
        auto_scaling: bool = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        send_receive_ratio: float = None,
        support_auto_scaling: bool = None,
    ):
        self.auto_scaling = auto_scaling
        self.message_retention_time = message_retention_time
        self.msg_process_spec = msg_process_spec
        self.send_receive_ratio = send_receive_ratio
        self.support_auto_scaling = support_auto_scaling

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        if self.support_auto_scaling is not None:
            result['supportAutoScaling'] = self.support_auto_scaling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        if m.get('supportAutoScaling') is not None:
            self.support_auto_scaling = m.get('supportAutoScaling')
        return self


class GetInstanceResponseBodyDataSoftware(TeaModel):
    def __init__(
        self,
        maintain_time: str = None,
        software_version: str = None,
        upgrade_method: str = None,
    ):
        self.maintain_time = maintain_time
        self.software_version = software_version
        self.upgrade_method = upgrade_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maintain_time is not None:
            result['maintainTime'] = self.maintain_time
        if self.software_version is not None:
            result['softwareVersion'] = self.software_version
        if self.upgrade_method is not None:
            result['upgradeMethod'] = self.upgrade_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maintainTime') is not None:
            self.maintain_time = m.get('maintainTime')
        if m.get('softwareVersion') is not None:
            self.software_version = m.get('softwareVersion')
        if m.get('upgradeMethod') is not None:
            self.upgrade_method = m.get('upgradeMethod')
        return self


class GetInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        account_info: GetInstanceResponseBodyDataAccountInfo = None,
        acl_info: GetInstanceResponseBodyDataAclInfo = None,
        bid: str = None,
        commodity_code: str = None,
        create_time: str = None,
        expire_time: str = None,
        ext_config: GetInstanceResponseBodyDataExtConfig = None,
        group_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_quotas: List[GetInstanceResponseBodyDataInstanceQuotas] = None,
        network_info: GetInstanceResponseBodyDataNetworkInfo = None,
        payment_type: str = None,
        product_info: GetInstanceResponseBodyDataProductInfo = None,
        region_id: str = None,
        release_time: str = None,
        remark: str = None,
        resource_group_id: str = None,
        series_code: str = None,
        service_code: str = None,
        software: GetInstanceResponseBodyDataSoftware = None,
        start_time: str = None,
        status: str = None,
        sub_series_code: str = None,
        topic_count: int = None,
        update_time: str = None,
        user_id: str = None,
    ):
        self.account_info = account_info
        self.acl_info = acl_info
        # BID
        self.bid = bid
        self.commodity_code = commodity_code
        self.create_time = create_time
        self.expire_time = expire_time
        self.ext_config = ext_config
        self.group_count = group_count
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_quotas = instance_quotas
        self.network_info = network_info
        self.payment_type = payment_type
        self.product_info = product_info
        self.region_id = region_id
        self.release_time = release_time
        self.remark = remark
        self.resource_group_id = resource_group_id
        self.series_code = series_code
        self.service_code = service_code
        self.software = software
        self.start_time = start_time
        self.status = status
        self.sub_series_code = sub_series_code
        self.topic_count = topic_count
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.account_info:
            self.account_info.validate()
        if self.acl_info:
            self.acl_info.validate()
        if self.ext_config:
            self.ext_config.validate()
        if self.instance_quotas:
            for k in self.instance_quotas:
                if k:
                    k.validate()
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()
        if self.software:
            self.software.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_info is not None:
            result['accountInfo'] = self.account_info.to_map()
        if self.acl_info is not None:
            result['aclInfo'] = self.acl_info.to_map()
        if self.bid is not None:
            result['bid'] = self.bid
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.ext_config is not None:
            result['extConfig'] = self.ext_config.to_map()
        if self.group_count is not None:
            result['groupCount'] = self.group_count
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        result['instanceQuotas'] = []
        if self.instance_quotas is not None:
            for k in self.instance_quotas:
                result['instanceQuotas'].append(k.to_map() if k else None)
        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.release_time is not None:
            result['releaseTime'] = self.release_time
        if self.remark is not None:
            result['remark'] = self.remark
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_code is not None:
            result['seriesCode'] = self.series_code
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.software is not None:
            result['software'] = self.software.to_map()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code
        if self.topic_count is not None:
            result['topicCount'] = self.topic_count
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountInfo') is not None:
            temp_model = GetInstanceResponseBodyDataAccountInfo()
            self.account_info = temp_model.from_map(m['accountInfo'])
        if m.get('aclInfo') is not None:
            temp_model = GetInstanceResponseBodyDataAclInfo()
            self.acl_info = temp_model.from_map(m['aclInfo'])
        if m.get('bid') is not None:
            self.bid = m.get('bid')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('extConfig') is not None:
            temp_model = GetInstanceResponseBodyDataExtConfig()
            self.ext_config = temp_model.from_map(m['extConfig'])
        if m.get('groupCount') is not None:
            self.group_count = m.get('groupCount')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        self.instance_quotas = []
        if m.get('instanceQuotas') is not None:
            for k in m.get('instanceQuotas'):
                temp_model = GetInstanceResponseBodyDataInstanceQuotas()
                self.instance_quotas.append(temp_model.from_map(k))
        if m.get('networkInfo') is not None:
            temp_model = GetInstanceResponseBodyDataNetworkInfo()
            self.network_info = temp_model.from_map(m['networkInfo'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('productInfo') is not None:
            temp_model = GetInstanceResponseBodyDataProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('software') is not None:
            temp_model = GetInstanceResponseBodyDataSoftware()
            self.software = temp_model.from_map(m['software'])
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')
        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInstanceResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        instance_id: str = None,
        message_type: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        topic_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.instance_id = instance_id
        self.message_type = message_type
        self.region_id = region_id
        self.remark = remark
        self.status = status
        self.topic_name = topic_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTopicResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetTopicResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTopicResponseBody = None,
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
            temp_model = GetTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumerGroupsRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.filter = filter
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListConsumerGroupsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        create_time: str = None,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.consumer_group_id = consumer_group_id
        self.create_time = create_time
        self.instance_id = instance_id
        self.region_id = region_id
        self.remark = remark
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListConsumerGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListConsumerGroupsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListConsumerGroupsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListConsumerGroupsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListConsumerGroupsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListConsumerGroupsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListConsumerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConsumerGroupsResponseBody = None,
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
            temp_model = ListConsumerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        self.filter = filter
        self.page_number = page_number
        self.page_size = page_size
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class ListInstancesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        create_time: str = None,
        expire_time: str = None,
        group_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        payment_type: str = None,
        region_id: str = None,
        release_time: str = None,
        remark: str = None,
        resource_group_id: str = None,
        series_code: str = None,
        service_code: str = None,
        start_time: str = None,
        status: str = None,
        sub_series_code: str = None,
        topic_count: int = None,
        update_time: str = None,
        user_id: str = None,
    ):
        self.commodity_code = commodity_code
        self.create_time = create_time
        self.expire_time = expire_time
        self.group_count = group_count
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.payment_type = payment_type
        self.region_id = region_id
        self.release_time = release_time
        self.remark = remark
        self.resource_group_id = resource_group_id
        self.series_code = series_code
        self.service_code = service_code
        self.start_time = start_time
        self.status = status
        self.sub_series_code = sub_series_code
        self.topic_count = topic_count
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.group_count is not None:
            result['groupCount'] = self.group_count
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.release_time is not None:
            result['releaseTime'] = self.release_time
        if self.remark is not None:
            result['remark'] = self.remark
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_code is not None:
            result['seriesCode'] = self.series_code
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code
        if self.topic_count is not None:
            result['topicCount'] = self.topic_count
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('groupCount') is not None:
            self.group_count = m.get('groupCount')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')
        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListInstancesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListInstancesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListInstancesResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListInstancesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTopicsRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        message_types: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.filter = filter
        self.message_types = message_types
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.message_types is not None:
            result['messageTypes'] = self.message_types
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('messageTypes') is not None:
            self.message_types = m.get('messageTypes')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListTopicsShrinkRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        message_types_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.filter = filter
        self.message_types_shrink = message_types_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.message_types_shrink is not None:
            result['messageTypes'] = self.message_types_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('messageTypes') is not None:
            self.message_types_shrink = m.get('messageTypes')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListTopicsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        instance_id: str = None,
        message_type: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        topic_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.instance_id = instance_id
        self.message_type = message_type
        self.region_id = region_id
        self.remark = remark
        self.status = status
        self.topic_name = topic_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListTopicsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListTopicsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListTopicsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTopicsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTopicsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListTopicsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListTopicsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTopicsResponseBody = None,
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
            temp_model = ListTopicsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConsumerGroupRequestConsumeRetryPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_topic: str = None,
        max_retry_times: int = None,
        retry_policy: str = None,
    ):
        self.dead_letter_target_topic = dead_letter_target_topic
        self.max_retry_times = max_retry_times
        self.retry_policy = retry_policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_topic is not None:
            result['deadLetterTargetTopic'] = self.dead_letter_target_topic
        if self.max_retry_times is not None:
            result['maxRetryTimes'] = self.max_retry_times
        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deadLetterTargetTopic') is not None:
            self.dead_letter_target_topic = m.get('deadLetterTargetTopic')
        if m.get('maxRetryTimes') is not None:
            self.max_retry_times = m.get('maxRetryTimes')
        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')
        return self


class UpdateConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        consume_retry_policy: UpdateConsumerGroupRequestConsumeRetryPolicy = None,
        delivery_order_type: str = None,
        remark: str = None,
    ):
        self.consume_retry_policy = consume_retry_policy
        self.delivery_order_type = delivery_order_type
        self.remark = remark

    def validate(self):
        if self.consume_retry_policy:
            self.consume_retry_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_retry_policy is not None:
            result['consumeRetryPolicy'] = self.consume_retry_policy.to_map()
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = UpdateConsumerGroupRequestConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m['consumeRetryPolicy'])
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConsumerGroupResponseBody = None,
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
            temp_model = UpdateConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequestNetworkInfoInternetInfo(TeaModel):
    def __init__(
        self,
        ip_whitelist: List[str] = None,
    ):
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class UpdateInstanceRequestNetworkInfo(TeaModel):
    def __init__(
        self,
        internet_info: UpdateInstanceRequestNetworkInfoInternetInfo = None,
    ):
        self.internet_info = internet_info

    def validate(self):
        if self.internet_info:
            self.internet_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internetInfo') is not None:
            temp_model = UpdateInstanceRequestNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m['internetInfo'])
        return self


class UpdateInstanceRequestProductInfo(TeaModel):
    def __init__(
        self,
        auto_scaling: bool = None,
        message_retention_time: int = None,
        send_receive_ratio: float = None,
    ):
        self.auto_scaling = auto_scaling
        self.message_retention_time = message_retention_time
        self.send_receive_ratio = send_receive_ratio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        network_info: UpdateInstanceRequestNetworkInfo = None,
        product_info: UpdateInstanceRequestProductInfo = None,
        remark: str = None,
    ):
        self.instance_name = instance_name
        self.network_info = network_info
        self.product_info = product_info
        self.remark = remark

    def validate(self):
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('networkInfo') is not None:
            temp_model = UpdateInstanceRequestNetworkInfo()
            self.network_info = temp_model.from_map(m['networkInfo'])
        if m.get('productInfo') is not None:
            temp_model = UpdateInstanceRequestProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceResponseBody = None,
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTopicRequest(TeaModel):
    def __init__(
        self,
        remark: str = None,
    ):
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTopicResponseBody = None,
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
            temp_model = UpdateTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


