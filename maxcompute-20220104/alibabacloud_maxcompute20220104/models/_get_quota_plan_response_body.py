# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetQuotaPlanResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetQuotaPlanResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetQuotaPlanResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetQuotaPlanResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        quota: main_models.GetQuotaPlanResponseBodyDataQuota = None,
    ):
        # The time when the quota plan was created.
        self.create_time = create_time
        # The name of the quota plan.
        self.name = name
        # The details of the quota.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.name is not None:
            result['name'] = self.name

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('quota') is not None:
            temp_model = main_models.GetQuotaPlanResponseBodyDataQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        return self

class GetQuotaPlanResponseBodyDataQuota(DaraModel):
    def __init__(
        self,
        billing_policy: main_models.GetQuotaPlanResponseBodyDataQuotaBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        schedule_info: main_models.GetQuotaPlanResponseBodyDataQuotaScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[main_models.GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the quota plan was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the quota.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The information of the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
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
            temp_model = main_models.GetQuotaPlanResponseBodyDataQuotaBillingPolicy()
            self.billing_policy = temp_model.from_map(m.get('billingPolicy'))

        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

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

        if m.get('scheduleInfo') is not None:
            temp_model = main_models.GetQuotaPlanResponseBodyDataQuotaScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('scheduleInfo'))

        if m.get('status') is not None:
            self.status = m.get('status')

        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k1 in m.get('subQuotaInfoList'):
                temp_model = main_models.GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList()
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

class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList(DaraModel):
    def __init__(
        self,
        billing_policy: main_models.GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        schedule_info: main_models.GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the user who created the quota plan.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The alias of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
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
            temp_model = main_models.GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m.get('billingPolicy'))

        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

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

        if m.get('scheduleInfo') is not None:
            temp_model = main_models.GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo()
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

class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo(DaraModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name

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

        return self

class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy(DaraModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
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

        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code

        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')

        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

class GetQuotaPlanResponseBodyDataQuotaScheduleInfo(DaraModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name

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

        return self

class GetQuotaPlanResponseBodyDataQuotaBillingPolicy(DaraModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
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

        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code

        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')

        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

