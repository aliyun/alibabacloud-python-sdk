# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class QueryQuotaResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryQuotaResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.QueryQuotaResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class QueryQuotaResponseBodyData(DaraModel):
    def __init__(
        self,
        billing_policy: main_models.QueryQuotaResponseBodyDataBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        group_name: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: main_models.QueryQuotaResponseBodyDataSaleTag = None,
        schedule_info: main_models.QueryQuotaResponseBodyDataScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[main_models.QueryQuotaResponseBodyDataSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        self.billing_policy = billing_policy
        self.cluster = cluster
        self.create_time = create_time
        self.creator_id = creator_id
        self.group_name = group_name
        self.id = id
        self.name = name
        self.nick_name = nick_name
        self.parameter = parameter
        self.parent_id = parent_id
        self.region_id = region_id
        self.sale_tag = sale_tag
        self.schedule_info = schedule_info
        self.status = status
        self.sub_quota_info_list = sub_quota_info_list
        self.tag = tag
        self.tenant_id = tenant_id
        self.type = type
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for v1 in self.sub_quota_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()

        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        if self.parameter is not None:
            result['parameter'] = self.parameter

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()

        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()

        if self.status is not None:
            result['status'] = self.status

        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k1 in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k1.to_map() if k1 else None)

        if self.tag is not None:
            result['tag'] = self.tag

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = main_models.QueryQuotaResponseBodyDataBillingPolicy()
            self.billing_policy = temp_model.from_map(m.get('billingPolicy'))

        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('saleTag') is not None:
            temp_model = main_models.QueryQuotaResponseBodyDataSaleTag()
            self.sale_tag = temp_model.from_map(m.get('saleTag'))

        if m.get('scheduleInfo') is not None:
            temp_model = main_models.QueryQuotaResponseBodyDataScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('scheduleInfo'))

        if m.get('status') is not None:
            self.status = m.get('status')

        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k1 in m.get('subQuotaInfoList'):
                temp_model = main_models.QueryQuotaResponseBodyDataSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k1))

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class QueryQuotaResponseBodyDataSubQuotaInfoList(DaraModel):
    def __init__(
        self,
        billing_policy: main_models.QueryQuotaResponseBodyDataSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        group_name: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: main_models.QueryQuotaResponseBodyDataSubQuotaInfoListSaleTag = None,
        schedule_info: main_models.QueryQuotaResponseBodyDataSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        self.billing_policy = billing_policy
        self.cluster = cluster
        self.create_time = create_time
        self.creator_id = creator_id
        self.group_name = group_name
        self.id = id
        self.name = name
        self.nick_name = nick_name
        self.parameter = parameter
        self.parent_id = parent_id
        self.region_id = region_id
        self.sale_tag = sale_tag
        self.schedule_info = schedule_info
        self.status = status
        self.tag = tag
        self.tenant_id = tenant_id
        self.type = type
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()

        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        if self.parameter is not None:
            result['parameter'] = self.parameter

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()

        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.tag is not None:
            result['tag'] = self.tag

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = main_models.QueryQuotaResponseBodyDataSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m.get('billingPolicy'))

        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('saleTag') is not None:
            temp_model = main_models.QueryQuotaResponseBodyDataSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m.get('saleTag'))

        if m.get('scheduleInfo') is not None:
            temp_model = main_models.QueryQuotaResponseBodyDataSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('scheduleInfo'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class QueryQuotaResponseBodyDataSubQuotaInfoListScheduleInfo(DaraModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        self.curr_plan = curr_plan
        self.curr_time = curr_time
        self.next_plan = next_plan
        self.next_time = next_time
        self.once_plan = once_plan
        self.once_time = once_time
        self.operator_name = operator_name
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan

        if self.curr_time is not None:
            result['currTime'] = self.curr_time

        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan

        if self.next_time is not None:
            result['nextTime'] = self.next_time

        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan

        if self.once_time is not None:
            result['onceTime'] = self.once_time

        if self.operator_name is not None:
            result['operatorName'] = self.operator_name

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')

        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')

        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')

        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')

        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')

        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')

        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

class QueryQuotaResponseBodyDataSubQuotaInfoListSaleTag(DaraModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.resource_ids = resource_ids
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class QueryQuotaResponseBodyDataSubQuotaInfoListBillingPolicy(DaraModel):
    def __init__(
        self,
        billing_method: str = None,
        instance_id: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        self.billing_method = billing_method
        self.instance_id = instance_id
        self.odps_spec_code = odps_spec_code
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code

        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

class QueryQuotaResponseBodyDataScheduleInfo(DaraModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        self.curr_plan = curr_plan
        self.curr_time = curr_time
        self.next_plan = next_plan
        self.next_time = next_time
        self.once_plan = once_plan
        self.once_time = once_time
        self.operator_name = operator_name
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan

        if self.curr_time is not None:
            result['currTime'] = self.curr_time

        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan

        if self.next_time is not None:
            result['nextTime'] = self.next_time

        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan

        if self.once_time is not None:
            result['onceTime'] = self.once_time

        if self.operator_name is not None:
            result['operatorName'] = self.operator_name

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')

        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')

        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')

        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')

        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')

        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')

        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

class QueryQuotaResponseBodyDataSaleTag(DaraModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.resource_ids = resource_ids
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class QueryQuotaResponseBodyDataBillingPolicy(DaraModel):
    def __init__(
        self,
        billing_method: str = None,
        instance_id: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        self.billing_method = billing_method
        self.instance_id = instance_id
        self.odps_spec_code = odps_spec_code
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code

        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

