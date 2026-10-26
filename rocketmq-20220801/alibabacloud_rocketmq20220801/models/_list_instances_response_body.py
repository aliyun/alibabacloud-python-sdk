# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListInstancesResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The response result.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID. Each request has a unique ID that you can use to troubleshoot and locate issues.
        self.request_id = request_id
        # Indicates whether the operation was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.ListInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

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

class ListInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListInstancesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The paged data.
        self.list = list
        # The current page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of returned results.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('list'):
                temp_model = main_models.ListInstancesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListInstancesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        create_time: str = None,
        expire_time: str = None,
        group_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        payment_type: str = None,
        product_info: main_models.ListInstancesResponseBodyDataListProductInfo = None,
        region_id: str = None,
        release_time: str = None,
        remark: str = None,
        resource_group_id: str = None,
        series_code: str = None,
        service_code: str = None,
        start_time: str = None,
        status: str = None,
        sub_series_code: str = None,
        tags: List[main_models.ListInstancesResponseBodyDataListTags] = None,
        topic_count: int = None,
        update_time: str = None,
        user_id: str = None,
    ):
        # The commodity code of the ApsaraMQ for RocketMQ 5.x series instance, such as ons_rmqsub_public_cn.
        self.commodity_code = commodity_code
        # The time when the instance version was last updated, in YYYY-MM-DD HH:mm:ss format.
        self.create_time = create_time
        # The time when the instance expires, in YYYY-MM-DD HH:mm:ss format.
        self.expire_time = expire_time
        # The number of consumer groups created in the instance.
        self.group_count = group_count
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The billing method of the instance. Valid values:
        # - PayAsYouGo: pay-as-you-go (postpaid).
        # - Subscription: subscription (prepaid).
        self.payment_type = payment_type
        # The product information.
        self.product_info = product_info
        # The ID of the region to which the instance belongs.
        self.region_id = region_id
        # The time when the instance was released, in YYYY-MM-DD HH:mm:ss format.
        self.release_time = release_time
        # The remarks for the instance.
        self.remark = remark
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The primary series code of the instance. Valid values:
        # - standard: Standard Edition.
        # - ultimate: Platinum Edition.
        # - professional: Professional Edition.
        # - shared: Shared Edition.
        # - dedicated: Dedicated Edition.
        self.series_code = series_code
        # The service code of the instance. The service code for ApsaraMQ for RocketMQ is rmq.
        self.service_code = service_code
        # The time when the instance was created, in YYYY-MM-DD HH:mm:ss format.
        self.start_time = start_time
        # The instance status. Valid values:
        # - RELEASED: Released.
        # - RUNNING: Running.
        # - STOPPED: Stopped.
        # - CHANGING: Changing.
        # - CREATING: Creating.
        self.status = status
        # The sub-series code of the instance. Valid values:
        # - cluster_ha: cluster high-availability edition.
        # - single_node: single-node edition.
        # - serverless: serverless edition.
        self.sub_series_code = sub_series_code
        # The resource tag list.
        self.tags = tags
        # The number of topics created in the instance.
        self.topic_count = topic_count
        # The time when the instance was last modified, in YYYY-MM-DD HH:mm:ss format.
        self.update_time = update_time
        # The ID of the user to whom the instance belongs.
        self.user_id = user_id

    def validate(self):
        if self.product_info:
            self.product_info.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

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

        if m.get('productInfo') is not None:
            temp_model = main_models.ListInstancesResponseBodyDataListProductInfo()
            self.product_info = temp_model.from_map(m.get('productInfo'))

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

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListInstancesResponseBodyDataListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class ListInstancesResponseBodyDataListTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the resource tag.
        self.key = key
        # The value of the resource tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListInstancesResponseBodyDataListProductInfo(DaraModel):
    def __init__(
        self,
        capacity_type: str = None,
        trace_on: bool = None,
    ):
        # The capacity mode. Valid values:
        # - provisioned: reserved capacity with elastic scaling.
        # - ondemand: pay-as-you-go.
        self.capacity_type = capacity_type
        # Specifies whether the message trace feature is enabled.
        # - true: The message trace feature is enabled.
        # - false: The message trace feature is disabled.
        # 
        # <props="intl">This parameter does not take effect. Regardless of whether this parameter is enabled, the instance supports the message trace feature by default.
        # <props="china">This parameter takes effect only for Serverless instances. If the message trace feature is enabled, message trace fees are incurred. For more information about billing, see [Serverless billing description](https://help.aliyun.com/document_detail/2586280.html).
        # 
        # <props="china">For pay-as-you-go and subscription instances, this parameter does not take effect. Regardless of whether this parameter is enabled, the message trace feature is supported by default.
        self.trace_on = trace_on

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_type is not None:
            result['capacityType'] = self.capacity_type

        if self.trace_on is not None:
            result['traceOn'] = self.trace_on

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capacityType') is not None:
            self.capacity_type = m.get('capacityType')

        if m.get('traceOn') is not None:
            self.trace_on = m.get('traceOn')

        return self

